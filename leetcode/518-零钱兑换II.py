# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 518-零钱兑换II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/10/19 2:33 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/10/19 2:33 下午
"""

"""
518. 零钱兑换 II
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
假设每一种面额的硬币有无限个。 
题目数据保证结果符合 32 位带符号整数。
"""


class Solution(object):

    def change(self, amount: int, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
