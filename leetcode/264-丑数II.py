# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 264-丑数II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/21 6:49 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/21 6:49 下午
"""

"""
264. 丑数II
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 或 5 的正整数。
"""


class Solution(object):
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2, p3, p5 = 1, 1, 1
        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp[n]
