# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 438-找到字符串中所有的字母异位词.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/8/27 4:51 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/8/27 4:51 下午
"""


class Solution(object):

    def findAnagrams(self, s: str, p: str):
        # 首先生成p的所有字母异位词， 然后在s中进行寻找
        # def generate_words(index):
        #     if index == len(p):
        #         ans.append(p[:])
        #         return
        #     for s_i in range(index, len(p)):
        #         p[index], p[s_i] = p[s_i], p[index]
        #         generate_words(index + 1)
        #         p[index], p[s_i] = p[s_i], p[index]
        #
        # ans, p = list(), [v for v in p]
        # generate_words(0)
        # p_list = [''.join(v) for v in ans]
        # res = []
        # for i in range(len(s) - len(p) + 1):
        #     if s[i: i + len(p)] in p_list:
        #         res.append(i)
        # return res
        len_s = len(s)
        len_p = len(p)
        if len_s < len_p:
            return
        order_s = [0] * 26
        order_p = [0] * 26
        ans = list()
        for i in range(len_p):
            order_s[ord(s[i]) - ord('a')] += 1
            order_p[ord(p[i]) - ord('a')] += 1
        if order_s == order_p:
            ans.append(0)
        for i in range(1, len_s - len_p + 1):
            order_s[ord(s[i + len_p - 1]) - ord('a')] += 1
            order_s[ord(s[i - 1]) - ord('a')] -= 1
            if order_s == order_p:
                ans.append(i)
        return ans


if __name__ == '__main__':
    Solution().findAnagrams("abab","ab")
