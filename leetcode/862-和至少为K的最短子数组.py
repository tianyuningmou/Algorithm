# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 862-和至少为K的最短子数组.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/11/4 10:50 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/11/4 10:50 上午
"""

import collections

class Solution(object):
    def shortestSubarray(self, nums, k: int) -> int:
        length = len(nums)
        P, ans = [0], length + 1
        for i in range(length):
            P.append(P[-1] + nums[i])
        monoq = collections.deque()
        for y, Py in enumerate(P):
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= k:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)
        return -1 if ans == length + 1 else ans


if __name__ == '__main__':
    print(Solution().shortestSubarray([84, -37, 32, 40, 95], 167))
