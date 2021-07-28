# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 733-图像渲染.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/7/25 2:57 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/7/25 2:57 下午
"""


class Solution(object):
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        row, column = len(image), len(image[0])
        currColor = image[sr][sc]

        def DFSFloodFill(mx, my, currColor, newColor):
            if image[mx][my] == currColor:
                image[mx][my] = newColor
                for mx, my in [(mx - 1, my), (mx + 1, my), (mx, my - 1), (mx, my + 1)]:
                    if 0 <= mx < row and 0 <= my < column and image[mx][my] == currColor:
                        DFSFloodFill(mx, my, currColor, newColor)

        if currColor != newColor:
            DFSFloodFill(sr, sc, currColor, newColor)
        return image


if __name__ == '__main__':
    print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
