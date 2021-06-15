# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 84-柱状图中最大的矩形.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/6/15 11:10 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/6/15 11:10 上午
"""

"""
84. 柱状图中最大的矩形
"""


class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
        print(left, right)
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans


if __name__ == '__main__':
    Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
