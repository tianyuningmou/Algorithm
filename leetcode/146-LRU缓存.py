# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 146-LRU缓存.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/11/22 2:07 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/11/22 2:07 下午
"""
import collections


class LRUCache(collections.OrderedDict):

    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def set(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
