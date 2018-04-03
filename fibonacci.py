# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: fibonacci.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/4/3 下午2:51

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/4/3 下午2:51
"""


# 斐波那契数列递归实现
def Fibonacci_Recursion(num):
    if num <= 1:
        return num
    return (Fibonacci_Recursion(num - 1) + Fibonacci_Recursion(num - 2))


# 斐波那契数列非递归实现
def Fibonacci_Not_Recursion(num):
    array = [0, 1]
    if num < 2:
        return array[num]
    for i in range(2, num + 1):
        array.append(array[i - 1] + array[i - 2])
    return array[num]


if __name__ == '__main__':
    num = 9
    result_one = Fibonacci_Recursion(num)
    result_two = Fibonacci_Not_Recursion(num)
    print(result_one == result_two)
