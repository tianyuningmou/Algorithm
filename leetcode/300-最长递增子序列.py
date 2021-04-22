# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 300-最长递增子序列.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/22 1:23 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/22 1:23 下午
"""

"""
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
"""


class Solution(object):
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [1] * length
        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
