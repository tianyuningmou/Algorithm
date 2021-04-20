# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 120-三角形最小路径和.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/20 6:45 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/20 6:45 下午
"""

"""
120. 三角形最小路径和
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
"""


class Solution(object):
    def minimumTotal(self, triangle) -> int:
        length = len(triangle)
        dp = [[0] * length for _ in range(length)]
        dp[0][0] = triangle[0][0]
        for i in range(1, length):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        return min(dp[length - 1])
