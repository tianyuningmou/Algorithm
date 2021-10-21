# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 440-字典序的第K小数字.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/10/21 3:01 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/10/21 3:01 下午
"""

"""
440. 字典序的第K小数字
给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。
注意：1 ≤ k ≤ n ≤ 109。
"""


class Solution(object):

    def findKthNumber(self, n: int, k: int) -> int:

        def calc_steps(n, n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n2, n + 1) - n1
                n1 *= 10
                n2 *= 10
            return steps

        cur = 1
        k -= 1
        while k > 0:
            steps = calc_steps(n, cur, cur + 1)
            if steps <= k:
                steps -= k
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur
