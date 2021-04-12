# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 456.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/1 6:28 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/1 6:28 下午
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
