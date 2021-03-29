# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 17.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/3/29 4:36 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/3/29 4:36 下午
"""


class Solution(object):

    @classmethod
    def letterCombinations(cls, digits: str):
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrace(index):
            if index == len(digits):
                combinations.append(''.join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrace(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrace(0)
        return combinations


if __name__ == '__main__':
    print(Solution.letterCombinations('235'))
