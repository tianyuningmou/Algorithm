# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 139-单词拆分.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/21 10:39 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/21 10:39 上午
"""

"""
139. 单词拆分
"""


class Solution(object):
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    Solution().wordBreak('leetcode', ['leet', 'code'])
