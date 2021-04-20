# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 45-跳跃游戏II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/20 4:46 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/20 4:46 下午
"""

"""
45. 跳跃游戏II
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
"""


class Solution(object):
    def reverse_jump(self, nums) -> int:
        position = len(nums) - 1
        stpes = 0
        while position > 0:
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    stpes += 1
                    break
        return stpes

    def jump(self, nums) -> int:
        max_pos, end, steps = 0, 0, 0
        for i in range(len(nums) - 1):
            if max_pos >= i:
                max_pos = max(max_pos, i + nums[i])
                if i == end:
                    max_pos = i
                    steps += 1
        return steps

