# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 456-132模式.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/1 6:28 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/1 6:28 下午
"""

"""
456. 132模式
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
"""


def find132pattern(nums) -> bool:
    n = len(nums)
    candidate_k = [nums[n - 1]]
    max_k = float("-inf")

    for i in range(n - 2, -1, -1):
        if nums[i] < max_k:
            return True
        while candidate_k and nums[i] > candidate_k[-1]:
            max_k = candidate_k[-1]
            candidate_k.pop()
        if nums[i] > max_k:
            candidate_k.append(nums[i])

    return False


if __name__ == '__main__':
    print(find132pattern([3, 4, 1, 2]))
