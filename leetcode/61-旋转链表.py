# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 61-旋转链表.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/28 4:44 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/28 4:44 下午
"""

"""
61. 旋转链表
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        pre = head
        length = 1
        while pre.next:
            length += 1
            pre = pre.next

        k = length - k % length
        pre.next = head
        while k:
            pre = pre.next
            k -= 1

        ret = pre.next
        pre.next = None
        return ret
