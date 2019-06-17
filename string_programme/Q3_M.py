# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: Q3_M.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2019-06-14 15:52

EMAIL: tianyuningmou2009@126.com

VERSION: : #1 
CHANGED By: : tianyuningmou
MODIFIED: : @Time : 2019-06-14 15:52
"""

"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度
"""


def solute(s: str):
    tmp_dict = dict()
    start, ans = 0, 0
    for end in range(len(s)):
        if s[end] in tmp_dict:
            start = max(tmp_dict[s[end]], start)
        ans = max(ans, end-start+1)
        tmp_dict[s[end]] = end + 1
    return ans


if __name__ == '__main__':
    print(solute('pwwkew'))
