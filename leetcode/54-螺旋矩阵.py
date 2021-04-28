# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 54-螺旋矩阵.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/28 3:51 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/28 3:51 下午
"""

"""
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""


class Solution(object):
    def spiralOrder(self, matrix):
        res_list = []
        if not matrix or not matrix[0]:
            return res_list
        row, col = len(matrix), len(matrix[0])
        visited = [[False] * row for _ in range(col)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex, row_i, col_j = 0, 0, 0
        for i in range(row * col):
            res_list.append(matrix[row_i][col_j])
            visited[row_i][col_j] = True
            newRow, newCol = row_i + directions[directionIndex][0], col_j + directions[directionIndex][1]
            if not (0 <= newRow < row and 0 <= newCol < col and not visited[newRow][newCol]):
                directionIndex = (directionIndex + 1) % 4
            row_i += directions[directionIndex][0]
            col_j += directions[directionIndex][1]
        return res_list


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
