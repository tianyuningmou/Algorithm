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
    # 先对给出的数据去重
    num_list = list(set(num_list))
    # 因为1可以当A用，且1开头的不算顺子
    if 1 in num_list:
        num_list.append(14)
        num_list.remove(1)
    # 2开头的不算顺子
    if 2 in num_list:
        num_list.remove(2)
    # 对整理后的数据进行从大到小排序
    num_list.sort(reverse=True)
    result_list = list()
    # 循环比对，找出顺子
    for num in range(1, len(num_list)):
        # 前后两个数相差为1，则把大的加入到result_list
        if num_list[num-1] - num_list[num] == 1:
            result_list.append(num_list[num-1])
            # 如果已经比对到最后一个数，则把最后一个数加入到列表
            if num == len(num_list) -1:
                result_list.append(num_list[num])
        # 前后相差不为1，把前一个加入列表
        else:
            result_list.append(num_list[num-1])
            # 此时如果已经多于五张牌，则已找到最大顺子，少于五张牌，把result_list清空，继续往下找
            if len(result_list) < 5:
                result_list = []
                continue
            else:
                break
    # 一遍查找之后，判断结果是否多于五张牌，是的话则找到最大顺子，如果不是，则这副牌中没有顺子
    if len(result_list) < 5:
        result_list = []
    # 对结果正向排序
    result_list.sort()
    # 替换到扑克牌中的表示
    result_list = [str(x) for x in result_list]
    result_list = ['A' if x == '14' else x for x in result_list]
    result_list = ['K' if x == '13' else x for x in result_list] 
    result_list = ['Q' if x == '12' else x for x in result_list]
    result_list = ['J' if x == '11' else x for x in result_list]
    return result_list


# 找出最长的顺子，并输出其长度
def find_max_length_straight(num_list):
    pass


if __name__ == '__main__':
    num_list = [1, 12, 11, 13]
    result = find_max_straight(num_list)
    print('此扑克牌中不存在顺子') if len(result) == 0 else print('扑克牌中的顺子为：{}'.format(result))
