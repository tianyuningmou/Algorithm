# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 200-岛屿数量.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/26 2:16 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/26 2:16 下午
"""

"""
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
"""


class Solution(object):
    def dfs(self, grid, x, y):
        grid[x][y] = '0'
        row, col = len(grid), len(grid[0])
        for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= x < row and 0 <= y < col and grid[x][y] == '1':
                self.dfs(grid, x, y)

    def numIslands(self, grid) -> int:
        row, col = len(grid), len(grid[0])
        numOfLands = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    numOfLands += 1
                    self.dfs(grid, x, y)
        return numOfLands
