# -*- coding: utf-8 -*-
# @Time    : 2022/9/30 10:28 上午
# @Author  : danica
# @FileName: json_ddt.py
# @Software: PyCharm

import json
import pytest


def get_data():
    with open('./data/json_data.json', 'r') as file:
        data = json.load(file)
        my_data = []
        my_data.extend(data['keys'])
        return my_data


@pytest.mark.parametrize('name', get_data())
def test(name):
    print(name)


if __name__ == '__main__':
    # print(get_data())
    pytest.main(['-sv', 'json_ddt.py'])
