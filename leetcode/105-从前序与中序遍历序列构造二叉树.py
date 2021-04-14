# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 105-从前序与中序遍历序列构造二叉树.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/1 10:55 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/1 10:55 上午
"""

"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树
"""

from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # 递归方式实现
    @classmethod
    def buildTreeRecursion(cls, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            # 前序遍历的第一个节点就是根节点
            preorder_root = preorder_left
            # 获取此节点在中序遍历中的位置
            inorder_root = inorder_dict[preorder[preorder_left]]
            root = TreeNode(preorder[preorder_left])
            size_left_subtree = inorder_root - inorder_left
            # 分别构建左右子树
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)
        inorder_dict = {value: index for index, value in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

    @classmethod
    def buildTreeIter(cls, preorder: List[int], inorder: List[int]) -> TreeNode:
        pass
