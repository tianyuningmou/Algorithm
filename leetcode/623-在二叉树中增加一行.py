# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 623-在二叉树中增加一行.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/19 3:28 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/19 3:28 下午
"""

"""
623. 在二叉树中增加一行
给定一个二叉树，根节点为第1层，深度为 1。在其第 d 层追加一行值为 v 的节点。
添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为 v 的左子树和右子树。
将 N 原先的左子树，连接为新节点 v 的左子树；将 N 原先的右子树，连接为新节点 v 的右子树。
如果 d 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 v，原先的整棵树将作为 v 的左子树。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def insert(root, val, depth, d):
            if not root:
                return None
            if d == depth - 1:
                temp = TreeNode(val)
                left = root.left
                root.left = temp
                root.left.left = left

                right = root.right
                root.right = temp
                root.right.right = right
            else:
                insert(root.left, val, depth, d + 1)
                insert(root.right, val, depth, d + 1)

        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        insert(root, val, depth, 1)
        return root
