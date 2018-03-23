# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: build_array.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/23 下午2:11

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/23 下午2:11
"""

class Solution:
    # 题目描述不清晰，没看太懂
    def multiply(self, A):
        first = [1]
        second = [1]
        for i in range(1, len(A)):
            # 依次保存中间的计算值
            first.append(first[i-1]*A[i-1])
            second.append(second[i-1]*A[-i])
        B = []
        for i in range(0, len(A)):
            B.append(first[i]*second[-(i+1)])
        return B

    def Add(self, num1, num2):
        # 使用sum函数
        return sum([num1, num2])


if __name__ == '__main__':
    solution = Solution()
    result0 = solution.multiply([1, 2, 3])
    result1 = solution.Add(2, 3)
    print(result0, '\n', result1)
