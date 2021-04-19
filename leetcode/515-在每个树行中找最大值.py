# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 515-在每个树行中找最大值.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/19 11:32 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/19 11:32 上午
"""

"""
515. 在每个树行中找最大值
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def largestValues(self, root: TreeNode):
        if not root:
            return []
        max_list = []
        res_list = [root]
        while res_list:
            max_ = float('-inf')
            for i in range(len(res_list)):
                node = res_list.pop(0)
                max_ = max(max_, node.val)
                if node.left:
                    res_list.append(node.left)
                if node.right:
                    res_list.append(node.right)
            max_list.append(max_)
        return max_list


if __name__ == '__main__':
    num_5 = TreeNode(5)
    num_3 = TreeNode(3)
    num_9 = TreeNode(9)
    num_4 = TreeNode(3, num_5, num_3)
    num_2 = TreeNode(2, right=num_9)
    num_1 = TreeNode(1, num_4, num_2)
    s = Solution()
    print(s.largestValues(num_1))
