# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: merge_sort.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/10 下午5:55

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/10 下午5:55
"""

"""
归并排序：
    将已经排好序的两个序列合并成一个
    
时间复杂度：O(n(logn/log2))
空间复杂度：O(1)
算法稳定性：稳定
"""


def merge_sort(list_one, list_two):
    length_one = len(list_one)
    length_two = len(list_two)
    list_three = []
    j = 0
    for i in range(length_one):
        while list_two[j] < list_one[i] and j < length_two:
            list_three.append(list_two[j])
            j += 1
        list_three.append(list_one[i])
    if j < (length_two - 1):
        for k in range(j, length_two):
            list_three.append(list_two[k])
    return list_three


if __name__ == '__main__':
    list_one = [1, 3, 5, 10]
    list_two = [2, 4, 5, 6, 8, 9, 11, 12, 13, 14]
    print(merge_sort(list_one, list_two))
