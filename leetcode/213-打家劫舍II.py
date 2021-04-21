# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 213-打家劫舍II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/21 3:51 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/21 3:51 下午
"""

"""
213. 打家劫舍II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
"""


class Solution(object):
    def rob(self, nums) -> int:
        def rob_cal(nums, start, end):
            first, second = nums[start], max(nums[start], nums[start + 1])
            for i in range(start + 2, end):
                first, second = second, max(first + nums[i], second)
            return second
        length = len(nums)
        if length <= 2:
            return max(nums)
        return max(rob_cal(nums, 0, len(nums) - 1), rob_cal(nums, 1, len(nums)))
