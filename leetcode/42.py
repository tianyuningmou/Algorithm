# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 42.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/3/27 3:25 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/3/27 3:25 下午
"""


def water(height):
    length = len(height)
    if length < 3:
        return 0
    ans, left_stack, right_stack = 0, [height[0]], [height[length - 1]] * length
    for i in range(1, length):
        left_stack.append(max(height[i], left_stack[i - 1]))
    for i in range(length - 2, -1, -1):
        right_stack[i] = max(height[i], right_stack[i + 1])
    for i in range(1, length):
        ans += min(left_stack[i], right_stack[i]) - height[i]
    return ans


if __name__ == '__main__':
    f = [[True] * 3 for _ in range(2)]
    f[1][1] = False
    print(f)
