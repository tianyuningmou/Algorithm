# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 189-旋转数组.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/7/21 2:43 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/7/21 2:43 下午
"""

"""
189. 旋转数组
"""


class Solution(object):
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
