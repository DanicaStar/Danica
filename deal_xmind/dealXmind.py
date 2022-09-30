# -*- coding: utf-8 -*-
# @Time    : 2021/3/17 16:44
# @Author  : danica
# @FileName: dealXmind.py
# @Software: PyCharm

import xmind, xmindparser
import json
import openpyxl
import sys


class DealXmind:
    oriCaseList = []

    def __init__(self):
        """
        初始化，获取文件名
        """
        with open('config.ini', 'r', encoding='utf-8') as f:
            self.xmindName = f.readline().split('=')[1].strip()
            self.version = f.readline().split('=')[1].strip()
            self.excelName = self.xmindName.split('.xmind')[0] + '.xlsx'
            self.xmindVersion = 8

    def dict_to_prettify_json(self, data):
        """
        xmind结果用json输出
        :param data:
        :return:
        """
        print(json.dumps(data, indent=4, separators=(',', ': ')))

    def test(self):
        self.dict_to_prettify_json(xmind.load(self.xmindName).getData()[0])
        # self.dict_to_prettify_json(xmindparser.xmind_to_dict(self.xmindName)[0])

    def doDeal(self):
        """
        执行xmind转excel
        :return:
        """
        destCaseList = self.getXmindInfo()
        self.down2Excel(destCaseList)

    def getXmindInfo(self):
        """
        分析处理xmind，转为[[目录，步骤1，步骤2.。。步骤n，用例名称，期望]]
        :return:
        """
        # 导入xmind
        xm = xmind.load(self.xmindName).getData()[0]
        self.caseName = xm['topic']['title']
        if self.caseName.find('Warning') != -1:
            xm = xmindparser.xmind_to_dict(self.xmindName)[0]
            self.caseName = xm['topic']['title']
            self.xmindVersion = 10
        xmindData = xm['topic']['topics']
        # 进行初步处理
        self.dealXmindData(xmindData)
        # 规整处理后的用例列表
        destCaseList = self.dealCaseStep()
        return destCaseList

    def dealXmindData(self, xmindData=[], singleCaseList=[], oriPreConfidence=''):
        """
        递归进行初步的xmind数据处理，将xmind整理为 目录，(前置条件)，步骤1，步骤2.。。步骤n，用例名称，期望的列表
        :param xmindData: 处理的xmind数据
        :param singleCaseList: 处理用例列表
        """
        try:
            for topic in xmindData:
                # 增加前置条件的获取
                preConfidence = 'confidence-{}'.format(topic.get('note', None))
                if len(singleCaseList) == 1:
                    singleCaseList.append(preConfidence)
                elif len(singleCaseList) > 1 and topic.get('note', None) is not None:
                    singleCaseList[1] = preConfidence
                # 增加步骤节点
                singleCaseList.append(topic['title'])
                if 'topics' in topic.keys():
                    # 如果有topics就深入一层
                    self.dealXmindData(topic['topics'], singleCaseList, preConfidence)
                else:
                    # 无topic就表示已经到叶子节点
                    # 先赋值给case，再把case保存，不然会是一个引用地址会在递归时候发生变化
                    case = singleCaseList[:]
                    # 获取打标信息
                    if self.xmindVersion == 8:
                        markers = topic.get('markers', [])
                    elif self.xmindVersion == 10:
                        markers = topic.get('makers', [])
                    else:
                        raise AssertionError('错误的xmind版本！')
                    # 处理打标信息
                    label, priority = self.dealMarkers(markers)
                    # 将标签和优先级加入到case信息中
                    case.append(label)
                    case.append(priority)
                    self.oriCaseList.append(case)
                # singleCaseList.remove(topic['title'])   # 可能会出现同名的步骤，改成最后删除最后1个元素
                singleCaseList.pop()  # 删除最后一个节点

                if topic.get('note', None) is not None and len(singleCaseList) > 1:
                    singleCaseList[1] = oriPreConfidence

                if len(singleCaseList) > 1 and singleCaseList[-1].find('confidence-') != -1:
                    singleCaseList.pop()  # 如果最后一个节点是前置条件，则删除
        except AssertionError as e:
            print(e)
            sys.exit()
        except Exception:
            tip = singleCaseList[0:1] + singleCaseList[2:-1]
            raise AssertionError('在用例整理中发生一点问题，涉及的用例如下：\n{}'.format('->'.join(tip)))

    def dealMarkers(self, markersList):
        """
        将打标信息进行处理为标签和优先级
        :param markersList: 需要处理的打标
        :return: 返回标签和优先级
        """
        label = self.version  # 标签信息，默认标签为版本号
        prority = 'P3'  # 优先级信息 默认优先级为P3

        # 红旗为冒烟
        # 冒烟优先级P0
        if 'flag-red' in markersList:
            label = label + ',冒烟'
            prority = 'P0'

        # 绿棋为回归
        # 回归优先级P1，如果有冒烟的P0，则不重置为P1
        if 'flag-green' in markersList:
            label = label + ',回归'
            if prority != 'P0':
                prority = 'P1'

        # 优先级标识只识别优先级最高的1个
        if 'priority-1' in markersList:
            prority = 'P1'
        elif 'priority-2' in markersList:
            prority = 'P2'
        elif 'priority-3' in markersList:
            prority = 'P3'
        elif 'priority-4' in markersList:
            prority = 'P4'

        return label, prority

    def dealCaseStep(self):
        """
        处理xmind生成的初步case，将步骤合并
        :return: 返回合并步骤后的caseList 格式为[[目录，前置步骤，步骤，用例名称，期望，标签，优先级]]
        """
        destCaseList = []
        for singleCase in self.oriCaseList:
            case = singleCase[:]
            confidence = ''  # 默认无前置条件
            # 设置前置条件，如果无前置条件则置空，否则截取confidence-后的数据
            if case[1].split('-')[1] != 'None':
                confidence = case[1].split('-')[1]
            # 默认步骤为空
            step = ''
            for index in range(2, len(case) - 4):
                step = step + str(index - 1) + '.' + case[index] + '\n'
            # 如果有步骤则需要将用例名称/期望/标签/优先级提前
            if step != '':
                case[1] = step.strip('\n')
                case[2] = case[-4]  # 用例名称
                case[3] = case[-3]  # 期望
                case[4] = case[-2]  # 标签
                case[5] = case[-1]  # 优先级
                # 将前置条件放着第二位置
                case.insert(1, confidence)
            else:
                # 如果无步骤 则手动增加需要增加1个元素
                case[1] = confidence  # 重设前置条件
                case.insert(2, '无步骤')
            destCaseList.append(case[0:7])

        return destCaseList

    def down2Excel(self, caseList):
        """
        将case输出到excel，
        :param caseList:标准化case入参，格式为[[目录，前置步骤，步骤，用例名称，期望，标签，优先级]]
        :return:
        """
        # 打开模板excel
        # modelWb = openpyxl.load_workbook('model.xlsx')
        # modelRowNameList = modelWb['Sheet1'][1]
        # 实例化
        wb = openpyxl.Workbook()
        # 激活 worksheet
        ws = wb.active
        # 选择默认创建的表
        table = wb['Sheet']
        # 设置列名
        table.append(['这是即将要导入的用例'])
        rowNameList = ['标题*', '目录层级', '前置条件', '步骤描述', '预期结果', '用例标签', '用例等级', '关联需求编号', '备注']
        table.append(rowNameList)
        table.append(['这个是用例库的规定，空他个一行'])
        # 分析case
        for case in caseList:
            excelCase = []
            # 设置用例名称
            excelCase.append(case[3])
            # 先设置目录
            dirList = case[0].replace('-', '|')  # 现在这个版本用例目录用|隔开
            excelCase.append(dirList)
            # 设置前置条件
            excelCase.append(case[1])
            # 设置步骤
            excelCase.append(case[2])
            # 设置期望结果
            excelCase.append(case[4])
            # 设置标签
            excelCase.append(case[5])
            # 设置优先级
            excelCase.append(case[6])
            # 将case保存到表格
            table.append(excelCase)
        # 保存文件
        wb.save(self.excelName)


if __name__ == '__main__':
    DealXmind().doDeal()
