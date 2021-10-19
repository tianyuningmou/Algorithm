# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 958-二叉树的完全性检验.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/10/19 3:14 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/10/19 3:14 下午
"""

"""
958. 二叉树的完全性检验
给定一个二叉树，确定它是否是一个完全二叉树。
百度百科中对完全二叉树的定义如下：
若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, v * 2))
                nodes.append((node.right, v * 2 + 1))
        return nodes[-1][1] == len(nodes)
