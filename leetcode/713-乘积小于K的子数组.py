# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 713-乘积小于K的子数组.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/8/30 2:20 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/8/30 2:20 下午
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    Solution().numSubarrayProductLessThanK([10,5,2,6], 100)