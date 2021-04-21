# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 279-完全平方数.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/21 7:03 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/21 7:03 下午
"""

"""
279-完全平方数
"""

import math

class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]
