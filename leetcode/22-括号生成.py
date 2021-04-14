# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 22-括号生成.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/3/29 5:12 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/3/29 5:12 下午
"""

"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合
"""


class Solution(object):

    @classmethod
    def generateParenthesis(cls, n: int):
        ans = []

        def backtrace(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
            if left < n:
                S.append('(')
                backtrace(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrace(S, left, right + 1)
                S.pop()

        backtrace([], 0, 0)
        return ans


if __name__ == '__main__':
    print(Solution.generateParenthesis(4))
