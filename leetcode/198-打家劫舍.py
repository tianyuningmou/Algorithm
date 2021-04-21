# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 198-打家劫舍.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/21 3:40 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/21 3:40 下午
"""

"""
198. 打家窃舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
"""


class Solution(object):
    def rob(self, nums) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

    def rob_two(self, nums) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, length):
            first, second = second, max(first + nums[i], second)
        return second
