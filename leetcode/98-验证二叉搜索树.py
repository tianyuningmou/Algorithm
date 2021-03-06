# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 98-验证二叉搜索树.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/3/31 11:25 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/3/31 11:25 上午
"""

"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @classmethod
    def isValidBST(cls, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


if __name__ == '__main__':
    tree_4 = TreeNode(4)
    tree_3 = TreeNode(3)
    tree_7 = TreeNode(7)
    tree_6 = TreeNode(6, tree_3, tree_7)
    tree_5 = TreeNode(5, tree_4, tree_6)
    Solution.isValidBST(tree_5)
