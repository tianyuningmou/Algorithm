# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: KMP.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/6/8 下午4:48

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/6/8 下午4:48
"""

# 字符串匹配

def get_next(p):
    next = [0 for i in range(len(p))]
    next[0] = -1
    i = 0
    k = -1
    while i < len(p) - 1:
        if k == -1 or p[i] == p[k]:
            i += 1
            k += 1
            next[i] = k
        else:
            k = next[k]
    return next


def KMP(s, p):
    if len(p) == 0:
        return 0
    next = get_next(p)
    i = 0
    j = 0
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(p):
        return i - len(p)
    else:
        return -1


if __name__ == '__main__':
    s = 'abdabc'
    p = 'abc'
    answer = KMP(s, p)
    print(answer)
