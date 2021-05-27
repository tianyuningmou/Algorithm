# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 77-组合.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/27 4:30 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/27 4:30 下午
"""

"""
77. 组合
"""


class Solution:
    def combine(self, n: int, k: int):

        def dfs(cur):
            if len(temp) + (n - cur + 1) < k:
                return
            if len(temp) == k:
                ans.append(temp[:])
                return
            # 选择当前
            temp.append(cur)
            dfs(cur + 1)
            temp.remove(temp[-1])
            # 不选择当前
            dfs(cur + 1)

        ans, temp = list(), list()
        dfs(1)
        return ans


if __name__ == '__main__':
    Solution().combine(4, 2)
