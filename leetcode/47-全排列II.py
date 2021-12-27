# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 47-全排列II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/19 11:11 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/19 11:11 上午
"""

"""
47. 全排列II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
"""


class Solution:
    def permuteUnique(self, nums):
        def backtrack(nums, ans, idx, perm):
            if idx == len(nums):
                ans.append(perm[:])
                return
            for i in range(len(nums)):
                if vis[i] or (i > 0 and nums[i] == nums[i - 1] and not vis[i - 1]):
                    continue
                perm.append(nums[i])
                vis[i] = True
                backtrack(nums, ans, idx + 1, perm)
                vis[i] = False
                perm.pop(idx)

        nums.sort()
        ans = []
        perm = []
        vis = [False] * len(nums)
        backtrack(nums, ans, 0, perm)
        return ans


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
