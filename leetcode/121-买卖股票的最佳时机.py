# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 121-买卖股票的最佳时机.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/22 4:08 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/22 4:08 下午
"""

"""
121. 买卖股票的最佳时机
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""


class Solution(object):
    def maxProfit(self, prices) -> int:
        minprice = 10000
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(price - minprice, maxprofit)
        return maxprofit
