# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 130-被围绕的区域.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/31 11:38 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/31 11:38 上午
"""

"""
130. 被围绕的区域
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
"""


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return

            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
