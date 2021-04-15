# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 5-最长回文子串.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/15 4:01 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/15 4:01 下午
"""

"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串 
"""

def longestPalindrome(s):
    length = len(s)
    dp = [[False] * length for _ in range(length)]
    ans = ''
    for s_len in range(length):
        for i in range(length):
            j = i + s_len
            if j >= length:
                break
            if s_len == 0:
                dp[i][j] = True
            elif s_len == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
            if dp[i][j] and s_len + 1 > len(ans):
                ans = s[i: j + 1]
    return ans


if __name__ == '__main__':
    print(longestPalindrome('babad'))
