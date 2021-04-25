# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 79-单词搜索.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/25 11:43 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/25 11:43 上午
"""

"""
79. 单词搜索
给定一个m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""


class Solution(object):
    def exist(self, board, word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.append((i, j))
            result = False
            for di, dj in directions:
                new_di, new_dj = i + di, j + dj
                if 0 <= new_di < board_i and 0 <= new_dj < board_j and (new_di, new_dj) not in visited:
                    if check(new_di, new_dj, k + 1):
                        result = True
                        break
            visited.remove((i, j))
            return result

        board_i, board_j = len(board), len(board[0])
        visited = []
        for i in range(board_i):
            for j in range(board_j):
                if check(i, j, 0):
                    return True
        return False
