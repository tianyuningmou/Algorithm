# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 445-两数相加II.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/6/16 6:16 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/6/16 6:16 下午
"""

"""
445. 两数相加II
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_stk, l2_stk = [], []
        while l1:
            l1_stk.append(l1.val)
            l1 = l1.next
        while l2:
            l2_stk.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while l1_stk or l2_stk or carry:
            l1_num = l1_stk.pop() if l1_stk else 0
            l2_num = l2_stk.pop() if l2_stk else 0
            value = l1_num + l2_num + carry
            cur_node = ListNode(value % 10, ans)
            carry = value // 10
            ans = cur_node
        return ans
