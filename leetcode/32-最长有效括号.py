# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 32-最长有效括号.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/10/19 2:50 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/10/19 2:50 下午
"""

"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
"""


class Solution(object):
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        ans, con = 0, [-1]
        for i in range(len(s)):
            if s[i] == '(':
                con.append(i)
            else:
                con.pop()
                if con:
                    ans = max(ans, i - con[-1])
                else:
                    con.append(i)
        return ans
