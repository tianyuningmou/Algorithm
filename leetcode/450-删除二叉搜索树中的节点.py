# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 450-删除二叉搜索树中的节点.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/16 2:30 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/16 2:30 下午
"""

"""
450. 删除二叉搜索树中的节点
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的key对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
    首先找到需要删除的节点；
    如果找到了，删除它。
说明：要求算法时间复杂度为O(h)，h 为树的高度
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root

