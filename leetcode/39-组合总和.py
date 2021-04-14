# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 39-组合总和.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/14 2:43 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/14 2:43 下午
"""

"""
39. 组合总和
给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates中的数字可以无限制重复被选取。

说明：
    所有数字（包括target）都是正整数。
    解集不能包含重复的组合。
"""


class Solution(object):
    def combinationSum(self, candidates, target: int):

        def dfs(candidates, target, combine, idx):
            if idx == len(candidates):
                return
            if target == 0:
                ans.append(combine[:])
                return
            dfs(candidates, target, combine, idx + 1)
            if target - candidates[idx] >= 0:
                combine.append(candidates[idx])
                dfs(candidates, target - candidates[idx], combine, idx)
                combine.pop()

        ans = []
        dfs(candidates, target, [], 0)
        return ans
