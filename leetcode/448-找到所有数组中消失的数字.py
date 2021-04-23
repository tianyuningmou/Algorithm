# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 448-找到所有数组中消失的数字.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/23 4:55 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/23 4:55 下午
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n

        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret


if __name__ == '__main__':
    Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
