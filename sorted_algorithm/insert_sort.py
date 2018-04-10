# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: insert_sort.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/10 下午5:24

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/10 下午5:24
"""

"""
插入排序：
    ①从第一个元素开始，该元素可以认为已经被排序
    ②取出下一个元素，在已经排序的元素中从后向前扫描
    ③如果该元素大于新元素，将该元素移到下一位置
    ④重复步骤③，直到排序完成
"""

def insert_sort(sort_list):
    count = len(sort_list)
    for i in range(1, count):
        key = sort_list[i]
        j = i - 1
        while j >= 0:
            if sort_list[j] > key:
                sort_list[j + 1] = sort_list[j]
                sort_list[j] = key
            j -= 1
    return sort_list


if __name__ == '__main__':
    list = [4, 7, 3, 8, 2]
    print(insert_sort(list))
