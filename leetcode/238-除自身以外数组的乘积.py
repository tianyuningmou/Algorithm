# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 238-除自身以外数组的乘积.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/27 10:37 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/27 10:37 上午
"""

"""
238. 除数组以外自身的乘积
"""


class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        L = [1] * length
        for left in range(1, length):
            L[left] = L[left - 1] * nums[left - 1]
        R = [1] * length
        for right in range(length - 2, -1, -1):
            R[right] = R[right + 1] * nums[right + 1]
        res = []
        for i in range(length):
            res.append(L[i] * R[i])
        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
