# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 49-字母异位词分组.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/7/19 9:33 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/7/19 9:33 下午
"""


import collections


class Solution(object):

    def groupAnagrams(self, strs):
        map_dict = dict()
        for str_ in strs:
            counts = ['0'] * 26
            for st in str_:
                st_num = int(counts[ord(st) - ord('a')])
                counts[ord(st) - ord('a')] = str(1 + st_num)
            if ''.join(counts) in map_dict:
                map_dict[''.join(counts)].append(str_)
            else:
                map_dict[''.join(counts)] = [str_]
        return list(map_dict.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
