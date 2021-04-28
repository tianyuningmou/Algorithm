# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 59-螺旋矩阵II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/28 4:16 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/28 4:16 下午
"""

"""
59. 螺旋矩阵II
"""


class Solution(object):
    def generateMatrix(self, n: int):
        row, col = n, n
        visited = [[False] * row for _ in range(col)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex, row_i, col_j = 0, 0, 0
        num = 1
        for i in range(row * col):
            visited[row_i][col_j] = num
            newRow, newCol = row_i + directions[directionIndex][0], col_j + directions[directionIndex][1]
            if not (0 <= newRow < row and 0 <= newCol < col and not visited[newRow][newCol]):
                directionIndex = (directionIndex + 1) % 4
            row_i += directions[directionIndex][0]
            col_j += directions[directionIndex][1]
            num += 1
        return visited
