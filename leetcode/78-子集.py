# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 78-子集.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/25 11:10 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/25 11:10 上午
"""

"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""


class Solution(object):
    def subsets(self, nums):
        def dfs(cur):
            if cur == length:
                ans.append(t[:])
                return
            t.append(nums[cur])
            dfs(cur + 1)
            t.pop()
            dfs(cur + 1)

        length = len(nums)
        t, ans = [], []
        dfs(0)
        return ans
