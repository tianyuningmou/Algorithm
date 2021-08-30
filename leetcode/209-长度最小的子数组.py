# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 209-长度最小的子数组.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/8/30 2:58 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/8/30 2:58 下午
"""

class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        if not nums:
            return 0
        length = len(nums)
        ans = length + 1
        total = left = right = 0
        while right < length:
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return 0 if ans == length + 1 else ans


if __name__ == '__main__':
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
