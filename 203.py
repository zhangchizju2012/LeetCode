#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:12:55 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 也可以in-place操作
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = ListNode(0)
        temp = node
        while head is not None:
            if head.val != val:
                temp.next = ListNode(head.val)
                temp = temp.next
            head = head.next
        return node.next
            