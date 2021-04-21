# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 221-最大正方形.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/21 6:20 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/21 6:20 下午
"""

class Solution(object):
    def maximalSquare(self, matrix) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        max_edge = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        print(i, j)
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_edge = max(max_edge, dp[i][j])
        return max_edge * max_edge


if __name__ == '__main__':
    Solution().maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
