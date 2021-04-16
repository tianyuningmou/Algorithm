# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 106-从中序与后序遍历序列构造二叉树.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/16 10:45 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/16 10:45 上午
"""

"""
106. 根据一棵树的中序遍历与后序遍历构造二叉树
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = key_dict[val]
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root

        key_dict = {val: index for index, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
