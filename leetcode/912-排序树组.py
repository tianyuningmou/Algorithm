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
            # 选取中间值为基准值
            pivot = (left + right) // 2
            # 将基准值和最后一个数更换位置
            nums[pivot], nums[right] = nums[right], nums[pivot]
            # 从左边开始迭代，比基准值nums[right]小的放在左边，并把left+1
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
            # 将左边界和基准值交换位置，此位置的左边都比基准值小，右边都比基准值大
            nums[left], nums[right] = nums[right], nums[left]
            return left

        sortArrayAll(nums, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    print(Solution().sortArray([5, 1, 1, 2, 0, 0]))
