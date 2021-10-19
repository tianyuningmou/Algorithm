# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 912-排序树组.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/10/19 4:36 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/10/19 4:36 下午
"""

import random

class Solution:
    def sortArray(self, nums):

        def sortArrayAll(nums, left, right):
            if left >= right:
                return
            mid = sortArraySingle(nums, left, right)
            sortArrayAll(nums, left, mid)
            sortArrayAll(nums, mid + 1, right)

        def sortArraySingle(nums, left, right):
            pivot = (left + right) // 2
            nums[pivot], nums[right] = nums[right], nums[pivot]
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
            nums[left], nums[right] = nums[right], nums[left]
            return left

        sortArrayAll(nums, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    print(Solution().sortArray([5, 1, 1, 2, 0, 0]))
