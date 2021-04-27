# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 347-前K个高频元素.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/27 2:15 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/27 2:15 下午
"""

"""
347. 前K个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
"""


class Solution(object):
    def topKFrequent(self, nums, k: int):
        num_dict = dict()
        for num in nums:
            if num in num_dict.keys():
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        num_dict = sorted(num_dict.items(), key=lambda x: -x[1])
        return [num[0] for num in num_dict[:k]]


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
