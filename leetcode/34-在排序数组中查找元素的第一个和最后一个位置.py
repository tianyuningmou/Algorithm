# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 34-在排序数组中查找元素的第一个和最后一个位置.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/14 11:10 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/14 11:10 上午
"""

"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
"""


class Solution:
    def searchRange(self, nums, target: int):

        def binarySearch(nums, target, lower):
            left, right, ans = 0, len(nums) - 1, len(nums)
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target or (lower and nums[mid] >= target):
                    right = mid - 1
                    ans = mid
                else:
                    left = mid + 1
            return ans

        leftIdx = binarySearch(nums, target, True)
        rightIdx = binarySearch(nums, target, False) - 1
        if leftIdx <= rightIdx < len(nums) and nums[leftIdx] == target and nums[rightIdx] == target:
            return [leftIdx, rightIdx]
        return [-1, -1]


if __name__ == '__main__':
    Solution().searchRange([2, 4, 6, 6, 7, 7, 8], 6)
