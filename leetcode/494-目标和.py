# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 494-目标和.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/10/1 11:01 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/10/1 11:01 上午
"""


class Solution(object):
    def findTargetSumWays(self, nums, target: int) -> int:

        def backtrack(nums, target, index, res):
            nonlocal count
            if index == len(nums):
                if res == target:
                    count += 1
            else:
                backtrack(nums, target, index + 1, res + nums[index])
                backtrack(nums, target, index + 1, res - nums[index])

        count = 0
        backtrack(nums, target, 0, 0)
        return count


if __name__ == '__main__':
    print(Solution().findTargetSumWays([47, 23, 35, 27, 30, 42, 26, 42, 30, 6, 8, 48, 44, 38, 41, 50, 18, 19, 19, 5],
                                       40))
