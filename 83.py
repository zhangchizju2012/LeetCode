#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:23:55 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        result = ListNode(0)
        temp = result
        data = None
        while head.next is not None:
            if head.val != data:
                temp.next = ListNode(head.val)
                temp = temp.next
            data = head.val
            head = head.next
        if head.val != data:
            temp.next = ListNode(head.val)
        return result.next