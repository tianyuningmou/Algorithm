# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 322-零钱兑换.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/15 5:45 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/15 5:45 下午
"""

"""
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回-1。
你可以认为每种硬币的数量是无限的。
"""


def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    print(coinChange([1, 2, 5], 11))
