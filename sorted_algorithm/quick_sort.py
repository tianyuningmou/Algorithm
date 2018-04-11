# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: quick_sort.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/11 上午9:21

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/11 上午9:21
"""

"""
快速排序：
    随意选择一个数字作为排序基准，比基准大的数字在右，比基准小的数字在左
    
时间复杂度：O(n(logn/log2))
空间复杂度：O(n(logn/log2))
算法稳定性：不稳定
"""

def quick_sort_all(sort_list, i, j):
    # 快速排序的整体函数，确定从哪排序
    if i < j:
        base = quick_sort(sort_list, i, j)
        quick_sort_all(sort_list, i, base)
        quick_sort_all(sort_list, base + 1, j)

def quick_sort(sort_list, i, j):
    base = sort_list[i]
    while i < j:
        while i < j and sort_list[j] >= base:
            j -= 1
        while i < j and sort_list[j] < base:
            sort_list[i] = sort_list[j]
            i += 1
            sort_list[j] = sort_list[i]
        sort_list[i] = base
    return i


if __name__ == '__main__':
    list = [4, 6, 8, 1, 3]
    quick_sort_all(list, 0, len(list) - 1)
    print(list)
