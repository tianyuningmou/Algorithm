# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 513-找树左下角的值.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/19 11:08 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/19 11:08 上午
"""

"""
513. 找树左下角的值
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res_list = [root]
        while res_list:
            node = res_list.pop(0)
            if node.right:
                res_list.append(node.right)
            if node.left:
                res_list.append(node.left)
        return node.val
