# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: bubble_sort.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/10 下午2:54

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/10 下午2:54
"""

"""
冒泡排序（从小到大）：
    ①比较相邻的元素。如果第一个比第二个大，就交换他们
    ②对每一对相邻元素作同样的工作，除了最后一个
    ③持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
    
时间复杂度：O(n**2)
空间复杂度：O(1)
算法稳定性：稳定
"""

def bubble_sort(sort_list):
    length = len(sort_list)
    for index in range(length):
        for i in range(1, length-index):
            if sort_list[i - 1] > sort_list[i]:
                sort_list[i -1], sort_list[i] = sort_list[i], sort_list[i - 1]
    return sort_list


if __name__ == '__main__':
    list = [2, 5, 6, 3]
    print(bubble_sort(list))
