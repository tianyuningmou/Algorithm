# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 24-两两交换链表中的节点.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/10 2:48 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/10 2:48 下午
"""


"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0, head)
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next
