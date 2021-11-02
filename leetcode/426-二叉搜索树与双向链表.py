# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 426-二叉搜索树与双向链表.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/11/1 11:54 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/11/1 11:54 上午
"""

"""
426. 二叉搜索树与双向链表
将二叉搜索树转换成双向链表
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def treeToDoublyList(self, root):

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if not root:
            return
        self.pre, self.head = None, None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

