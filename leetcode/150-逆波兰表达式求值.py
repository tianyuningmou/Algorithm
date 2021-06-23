# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 150-逆波兰表达式求值.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/6/23 6:14 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/6/23 6:14 下午
"""

"""
150. 逆波兰表达式求值
"""


class Solution(object):
    def evalRPN(self, tokens) -> int:
        flags = {'+': 1, '-': 2, '*': 3, '/': 4}
        stack = []
        for token in tokens:
            if token not in flags.keys():
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if flags[token] == 1:
                    res = num1 + num2
                elif flags[token] == 2:
                    res = num1 - num2
                elif flags[token] == 3:
                    res = num1 * num2
                else:
                    res = num1 / num2
                stack.append(res)
        return stack.pop()


if __name__ == '__main__':
    Solution().evalRPN(["4","13","5","/","+"])
