# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 538-把二叉搜索树转换为累加树.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/19 2:18 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/19 2:18 下午
"""

"""
538. 把二叉搜索树转换为累加树
给出二叉 搜索 树的根节点，该树的节点值各不相同。
请你将其转换为累加树（Greater Sum Tree）使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)

        total = 0
        dfs(root)
        return root
