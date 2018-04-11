# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: count_sort.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/11 上午9:53

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/11 上午9:53
"""

"""
计数排序
"""

def count_sort(sort_list):
    max = min = 0
    for i in sort_list:
        if i < min:
            min = i
        if i > max:
            max = i
    count = [0] * (max - min + 1)
    for index in range(max - min + 1):
        count[index] = 0
    for j in sort_list:
        count[j - min] += 1
    index = 0
    for k in range(max - min + 1):
        for c in range(count[k]):
            sort_list[index] = k + min
            index += 1
    return sort_list


if __name__ == '__main__':
    list = [3, 5, 8, 6, 1]
    print(count_sort(list))
