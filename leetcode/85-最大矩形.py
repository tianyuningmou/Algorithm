# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 85-最大矩形.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/6/17 2:42 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/6/17 2:42 下午
"""


"""
85. 最大矩形
"""


class Solution:
    def maximalRectangle(self, matrix) -> int:
        row = len(matrix)
        if row == 0:
            return 0
        col = len((matrix[0]))
        left = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    left[i][j] = 1 if j == 0 else left[i][j - 1] + 1
        ret = 0
        for j in range(col):
            up = [0 for _ in range(row)]
            down = [0 for _ in range(row)]
            stack = []
            for i in range(row):
                while stack and left[stack[-1]][j] >= left[i][j]:
                    stack.pop()
                up[i] = -1 if not stack else stack[-1]
                stack.append(i)
            stack = []
            for i in range(row - 1, -1, -1):
                while stack and left[stack[-1]][j] >= left[i][j]:
                    stack.pop()
                down[i] = row if not stack else stack[-1]
                stack.append(i)
            for i in range(row):
                height = down[i] - up[i] - 1
                area = height * left[i][j]
                ret = max(ret, area)
        return ret


if __name__ == '__main__':
    Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
