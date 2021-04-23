# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 55-跳跃游戏.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/23 6:03 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/23 6:03 下午
"""

"""
55. 跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
"""


class Solution(object):
    def canJump(self, nums) -> bool:
        length, mostRight = len(nums), 0
        for i in range(length):
            if i <= mostRight:
                mostRight = max(mostRight, i + nums[i])
                if mostRight >= length - 1:
                    return True
        return False
