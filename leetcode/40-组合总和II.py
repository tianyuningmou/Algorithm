# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 40-组合总和II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/18 4:00 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/18 4:00 下午
"""

"""
40. 组合总和II
给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates中的每个数字在每个组合中只能使用一次。

说明：
    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。
"""

import collections


class Solution(object):
    def combinationSum2(self, candidates, target: int):
        def dfs(pos: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return

            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]

        freq = sorted(collections.Counter(candidates).items())
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans
