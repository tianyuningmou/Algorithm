# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: string_operate.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/9 下午2:20

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/9 下午2:20
"""


class Solutiion(object):

    def str_to_int(self, str_content):
        if not str_content:
            return '未输入字符串'
        str2num = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
        flag2num = {'-':-1, '+': 1}
        first = str_content[0]
        if first in ['+', '-']:
            flag = flag2num[first]
            tmp = 0
            for n in str_content[1:]:
                if n not in str2num.keys():
                    return '不能转换成对应的数字'
                tmp = tmp * 10 + str2num[n]
            return tmp * flag
        else:
            tmp = 0
            for n in str_content:
                if n not in str2num.keys():
                    return '不能转换成对应的数字'
                tmp = tmp * 10 + str2num[n]
            return tmp


if __name__ == '__main__':
    solution = Solutiion()
    print(solution.str_to_int(''))
    print(solution.str_to_int('345'))
    print(solution.str_to_int('-345'))
    print(solution.str_to_int('-3a5'))
