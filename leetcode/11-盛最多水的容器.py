# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 11-盛最多水的容器.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/15 4:20 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/15 4:20 下午
"""

"""
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。
"""


def maxArea(height):
    ans = 0
    left, right = 0, len(height) - 1
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        ans = max(ans, water)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return ans


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
