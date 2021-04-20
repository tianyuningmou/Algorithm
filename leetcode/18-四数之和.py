# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 18-四数之和.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/20 2:27 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/20 2:27 下午
"""

"""
18.四数之和
找出所有满足条件不重复的四元组满足 a + b + c + d = target
"""


class Solution(object):
    def fourSum(self, nums, target: int):
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets

        # 数据进行排序
        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 如果最小的四个数都大于目标值，直接结束
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 如果i + 最大的三个小于目标值，i + 1
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets
