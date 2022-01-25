# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 0-二叉树的遍历.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2022/1/11 11:37 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2022/1/11 11:37 上午
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    @classmethod
    def preorder(cls, root):
        preorder_list, stk = list(), list()
        while root or stk:
            while root:
                preorder_list.append(root.val)
                stk.append(root)
                root = root.left
            root = stk.pop()
            root = root.right
        return preorder_list

    @classmethod
    def inorder(cls, root):
        inorder_list, stk = list(), list()
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            inorder_list.append(root.val)
            root = root.right
        return inorder_list

    @classmethod
    def postorder(cls, root):
        postorder_list, stk, prev = list(), list(), None
        # while root or stk:
        #     while root:
        #         stk.append(root)
        #         root = root.left
        #     root = stk.pop()
        #     if not root.right or root.right == prev:
        #         postorder_list.append(root.val)
        #         prev = root
        #         root = None
        #     else:
        #         stk.append(root)
        #         root = root.right
        # return postorder_list

        while root or stk:
            while root:
                postorder_list.append(root.val)
                stk.append(root)
                root = root.right
            root = stk.pop()
            root = root.left
        return postorder_list[::-1]


if __name__ == '__main__':
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    two = TreeNode(2, four, five)
    three = TreeNode(3, six, seven)
    one = TreeNode(1, two, three)
    print(Solution.postorder(one))
