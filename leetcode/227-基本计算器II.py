# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 227-基本计算器II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/6/24 10:34 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/6/24 10:34 上午
"""

"""
227. 基本计算器II
"""


class Solution(object):
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preSign = s[i]
                num = 0
        return sum(stack)


if __name__ == '__main__':
    Solution().calculate('3+5 / 2')
