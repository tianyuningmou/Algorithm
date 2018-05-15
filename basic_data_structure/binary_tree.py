# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: binary_tree.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/5/15 上午11:06

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/5/15 上午11:06
"""

"""
二叉树是每个节点最多有两个子树的树结构，子树有左右之分，二叉树常被用于实现二叉查找树和二叉堆
    深度为 k, 且有 2**k-1 个节点称之为满二叉树；
    深度为 k，有 n 个节点的二叉树，当且仅当其每一个节点都与深度为 k 的满二叉树中序号为 1 至 n 的节点对应时，称之为完全二叉树。
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Traversal:

    def __init__(self):
        self.traverse_path = list()

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)
