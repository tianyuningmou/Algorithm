# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 143-重排链表.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/5/31 2:21 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/5/31 2:21 下午
"""

"""
143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1

        vec[i].next = None
