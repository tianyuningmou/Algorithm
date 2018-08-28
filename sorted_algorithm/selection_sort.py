# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: selection_sort.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/10 下午5:18

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/10 下午5:18
"""

"""
选择排序：
    从待排序的数据元素中选出最小(最大)的元素，放在序列的起始位置，直到全部待排序的数据元素排完

时间复杂度：O(n**2)
空间复杂度：O(1)
算法稳定性：不稳定
"""


def selection_sort(sort_list):
    length = len(sort_list)
    for index in range(length):
        for i in range(index, length):
            if sort_list[index] > sort_list[i]:
                sort_list[index], sort_list[i] = sort_list[i], sort_list[index]
    return sort_list


if __name__ == '__main__':
    list = [3, 6, 4, 1]
    print(selection_sort(list))
