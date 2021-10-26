# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 556-下一个更大元素III.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/10/26 11:45 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/10/26 11:45 上午
"""


class Solution(object):
    def nextGreaterElement(self, nums: int) -> int:
        ori = nums
        nums = [v for v in str(nums)]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return int(''.join(nums)) if str(ori) != ''.join(nums) else -1


if __name__ == '__main__':
    Solution().nextGreaterElement(2147483486)
