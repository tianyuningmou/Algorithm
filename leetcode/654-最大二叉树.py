# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 654-最大二叉树.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/19 4:21 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/19 4:21 下午
"""

"""
654. 最大二叉树
给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 
定义如下：
    二叉树的根是数组 nums 中的最大元素。
    左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
    右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
    返回有给定数组 nums 构建的 最大二叉树 。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums) -> TreeNode:

        def get_max_index(nums, left, right):
            max_index = left
            for i in range(left, right):
                if nums[i] > nums[max_index]:
                    max_index = i
            return max_index

        def construct(nums, left, right):
            if left == right:
                return None
            max_index = get_max_index(nums, left, right)
            node = TreeNode(nums[max_index])
            node.left = construct(nums, left, max_index)
            node.right = construct(nums, max_index + 1, right)
            return node

        return construct(nums, 0, len(nums))
