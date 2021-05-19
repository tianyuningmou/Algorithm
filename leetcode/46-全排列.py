# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 46-全排列.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/19 10:28 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/19 10:28 上午
"""

"""
46. 全排列
给定一个不含重复数字的数组nums，返回其所有可能的全排列。你可以按任意顺序返回答案。
"""


class Solution(object):
    def permute(self, nums):
        def backtrace(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrace(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrace()
        return res


if __name__ == '__main__':
    Solution().permute([1, 2, 3])
