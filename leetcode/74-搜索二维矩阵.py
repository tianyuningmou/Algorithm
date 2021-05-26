# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 74-搜索二维矩阵.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/26 3:55 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/26 3:55 下午
"""

"""
74. 搜索二维矩阵
"""


class Solution(object):
    def searchMatrix(self, matrix, target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        row_left, row_right = -1, row - 1
        while row_left < row_right:
            middle = (row_right - row_left + 1) // 2 + row_left
            if target >= matrix[middle][0]:
                row_left = middle
            else:
                row_right = middle - 1
        col_left, col_right = 0, col - 1
        while col_left <= col_right:
            middle = (col_right - col_left) // 2 + col_left
            if target > matrix[row_left][middle]:
                col_left = middle + 1
            elif target < matrix[row_left][middle]:
                col_right = middle - 1
            else:
                return True
        return False


if __name__ == '__main__':
    Solution().searchMatrix([[1]], 1)
