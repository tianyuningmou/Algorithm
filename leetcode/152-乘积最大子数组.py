# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 152-乘积最大子数组.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/21 3:34 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/21 3:34 下午
"""

"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
"""


class Solution(object):
    def maxProduct(self, nums) -> int:
        dp_max, dp_min = nums[0], nums[0]
        maxp = nums[0]
        for i in range(1, len(nums)):
            dp_max, dp_min = max(nums[i], dp_max*nums[i], dp_min*nums[i]), min(nums[i], dp_max*nums[i], dp_min*nums[i])
            maxp = max(maxp, dp_max)
        return maxp
