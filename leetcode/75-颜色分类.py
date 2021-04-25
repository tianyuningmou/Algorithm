# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 75-颜色分类.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/25 10:49 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/25 10:49 上午
"""

"""
75. 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
"""


class Solution(object):
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        p0, p2 = 0, length - 1
        for i in range(length):
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1

