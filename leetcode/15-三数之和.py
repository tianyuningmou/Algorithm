# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 15-三数之和.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/15 4:46 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/15 4:46 下午
"""

"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""

def threeSum(nums):
    length = len(nums)
    ans = []
    nums.sort()

    for i in range(length):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        third = length - 1
        for second in range(i + 1, length):
            if second > i + 1 and nums[second] == nums[second - 1]:
                continue
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            if second >= third:
                break
            if nums[second] + nums[third] == target:
                ans.append([nums[i], nums[second], nums[third]])
    return ans


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
