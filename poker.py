# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: poker.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/15 下午4:37

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/15 下午4:37
"""

# 找出最大的顺子
def find_max_straight(num_list):
    num_list = list(set(num_list))
    if 1 in num_list:
        num_list.append(14)
        num_list.remove(1)
    if 2 in num_list:
        num_list.remove(2)
    num_list.sort(reverse=True)
    result_list = list()
    for num in range(1, len(num_list)):
        if num_list[num-1] - num_list[num] == 1:
            result_list.append(num_list[num-1])
            if num == len(num_list) -1:
                result_list.append(num_list[num])
        else:
            result_list.append(num_list[num-1])
            if len(result_list) < 5:
                result_list = []
                continue
            else:
                break
    if len(result_list) < 5:
        result_list = []
    result_list.sort()
    result_list = [str(x) for x in result_list]
    result_list = ['A' if x == '14' else x for x in result_list]
    result_list = ['K' if x == '13' else x for x in result_list] 
    result_list = ['Q' if x == '12' else x for x in result_list]
    result_list = ['J' if x == '11' else x for x in result_list]
    return result_list

if __name__ == '__main__':
    num_list = [1, 12, 11, 13]
    result = find_max_straight(num_list)
    print('此扑克牌中不存在顺子') if len(result) == 0 else print('扑克牌中的顺子为：{}'.format(result))
