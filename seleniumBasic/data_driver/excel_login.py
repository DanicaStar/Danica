# -*- coding:utf-8 -*-
# @Time : 2020-12-26 10:28
# @Author: Danica
# @File : excel_login.py

import openpyxl,unittest,requests,json,jsonpath

class MyCase(unittest.TestCase):
    data=[]
    @classmethod
    def setUpClass(cls) -> None:
        wk=openpyxl.load_workbook(r'excel_login.xlsx')
        sheet=wk['Sheet1']
        rows_sheet=sheet.iter_rows()

        for item in rows_sheet:
            if item[0].value=='url':
                continue
            list=[]
            for col in item:
                list.append(col.value)
            MyCase.data.append(list)
            print(MyCase.data)

    def test_checklist(self):
        for checklist in MyCase.data:
            url=checklist[0]
            expect=checklist[2]
            jsondir=checklist[3]
            res=requests.get(url)
            resjson=json.loads(res.content)
            result = jsonpath.jsonpath(resjson, jsondir)
            print(resjson)
            self.assertEqual(expect, result[0])

if __name__ == '__main__':
    unittest.main()
