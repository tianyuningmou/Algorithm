# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: head_sort.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/11 上午9:38

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/11 上午9:38
"""

"""
堆排序：
    堆排序利用了堆这种数据机构所设计的一种排序算法，堆是一个类似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

堆排序的步骤：
    ①创建最大堆：将堆所有数据重新排序，使其成为最大堆
    ②最大堆调整：作用是保持最大堆的性质，是创建最大堆的核心子程序
    ③堆排序：移除位在第一个数据的根节点，并做最大堆调整的递归运算
"""

def head_sort(sort_list):
    length = len(sort_list)
    first = int(length / 2 -1)
    for start in range(first, -1, -1):
        max_headify(sort_list, start, length - 1)
    for end in range(length - 1, 0, -1):
        sort_list[end], sort_list[0] = sort_list[0], sort_list[end]
        max_headify(sort_list, 0, end - 1)
    return sort_list

def max_headify(sort_list, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and sort_list[child] < sort_list[child + 1]:
            child = child + 1
        if sort_list[root] < sort_list[child]:
            sort_list[root], sort_list[child] = sort_list[child], sort_list[root]
            root = child
        else:
            break


if __name__ == '__main__':
    list = [3, 4, 8, 6, 1]
    print(head_sort(list))
