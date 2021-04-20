# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 16-最接近的三数之和.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/20 2:13 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/20 2:13 下午
"""

"""
16. 最接近的三数之和
给定数组，求出数组中三个数之和与target最接近
"""


class Solution(object):
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        length = len(nums)
        res = 10000

        def update_res(total):
            nonlocal res
            if abs(res - target) > abs(total - target):
                res = total

        for first in range(length):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second, third = first + 1, length - 1
            while second < third:
                total = nums[first] + nums[second] + nums[third]
                if total == target:
                    return total
                update_res(total)
                if total < target:
                    second_ = second + 1
                    while second_ < third and nums[second_] == nums[second]:
                        second_ += 1
                    second = second_
                if total > target:
                    third_ = third - 1
                    while third_ > second and nums[third_ ] == nums[third]:
                        third_ -= 1
                    third = third_
        return res


if __name__ == '__main__':
    Solution().threeSumClosest([-1,2,1,-4], 1)
