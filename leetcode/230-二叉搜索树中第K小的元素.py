# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 230-二叉搜索树中第K小的元素.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/13 2:15 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/13 2:15 下午
"""
"""
230. 二叉搜索树中第K小的元素
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        while True:
            while root:
                res.append(root)
                root = root.left
            node = res.pop()
            k -= 1
            if not k:
                return node.val
            root = node.right
