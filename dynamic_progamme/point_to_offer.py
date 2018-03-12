# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: point_to_offer.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/12 上午11:59

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/12 上午11:59
"""


class Solution:
    # 找到和为s的数字
    def find_numbers_with_sum(self, array, sum):
        # 如果数组为空，则返回空结果
        if not array:
            return []
        # 对传进来的数组进行排序
        array = sorted(array)
        # 设置两个指针，low只加，high只减
        low = 0
        high = len(array) - 1
        result_all = list()
        # 找出所有和为s的组合
        while low < high:
            tmp_sum = array[low] + array[high]
            if tmp_sum > sum:
                high -= 1
            elif tmp_sum < sum:
                low += 1
            else:
                result = (array[low], array[high])
                result_all.append(result)
                low += 1
                continue
        return result_all


if __name__ == '__main__':
    solution = Solution()
    result = solution.find_numbers_with_sum([2, 5, 3, 9, 7], 12)
    print(result)
