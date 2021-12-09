# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 239-滑动窗口最大值.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/12/6 6:42 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/12/6 6:42 下午
"""


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        sliding_list = list()
        for i in range(k):
            while sliding_list and nums[i] >= nums[sliding_list[-1]]:
                sliding_list.pop()
            sliding_list.append(i)

        ans = [nums[sliding_list[0]]]
        for i in range(k, len(nums)):
            while sliding_list and nums[i] >= nums[sliding_list[-1]]:
                sliding_list.pop()
            sliding_list.append(i)
            while sliding_list and sliding_list[0] <= i - k:
                sliding_list.pop(0)
            ans.append(nums[sliding_list[0]])
        return ans


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
