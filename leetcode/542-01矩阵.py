# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 542-01矩阵.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/7/28 11:51 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/7/28 11:51 上午
"""

"""
542. 01矩阵
"""


class Solution:
    def updateMatrix(self, mat):
        row, column = len(mat), len(mat[0])
        ans = [[0] * column for _ in range(row)]
        queue = [(i, j) for i in range(row) for j in range(column) if mat[i][j] == 0]
        seen_set = set(queue)

        while queue:
            i, j = queue.pop(0)
            for mi, mj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= mi < row and 0 <= mj < column and (mi, mj) not in seen_set:
                    ans[mi][mj] = mat[i][j] + 1
                    queue.append((mi, mj))
                    seen_set.add((mi, mj))
        return ans


if __name__ == '__main__':
    Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
