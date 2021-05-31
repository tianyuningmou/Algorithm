# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 128-最长连续序列.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/31 11:24 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/31 11:24 上午
"""

"""
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？
"""


class Solution(object):
    def longestConsecutive(self, nums) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
