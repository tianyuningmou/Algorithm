# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 416-分割等和子集.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/27 4:57 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/27 4:57 下午
"""

"""
416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
"""


class Solution(object):
    def canPartition(self, nums) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]
