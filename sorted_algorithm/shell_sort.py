# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: shell_sort.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/10 下午5:42

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/10 下午5:42
"""

"""
希尔排序：
    先取一个小于n的整数d1作为第一个增量，把文件的全部记录分组。所有距离为d1的倍数的记录放在同一个组中。先在各组内进行直接插入排序；
    然后，取第二个增量d2<d1，重复上述的分组和排序，直到排序完成。
"""

def shell_sort(sort_list):
    length = len(sort_list)
    dist = int(length / 2)
    while dist > 0:
        for i in range(dist, length):
            temp = sort_list[i]
            j = i
            while j >= dist and temp < sort_list[j - dist]:
                sort_list[j] = sort_list[j-dist]
                j -= dist
            sort_list[j] = temp
        dist = int(dist / 2)
    return sort_list

if __name__ == '__main__':
    list = [3, 4, 1, 6]
    print(shell_sort(list))
