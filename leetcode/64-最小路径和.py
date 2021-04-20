# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 64-最小路径和.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/20 6:23 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/20 6:23 下午
"""

"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
"""


class Solution(object):
    def minPathSum(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for j in range(1, row):
            dp[j][0] = dp[j - 1][0] + grid[j][0]
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[row - 1][col - 1]
