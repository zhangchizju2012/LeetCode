#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:32:24 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        first = head
        second = head.next
        while first != second:
            if second.next is not None and second.next.next is not None:
                second = second.next.next
            else:
                return False
            first = first.next
        return True
            

#==============================================================================
# a = ListNode(3)
# 
# a.next = ListNode(4)
# 
# a.next.next = ListNode(5)
# 
# a.next.next.next = ListNode(4)
# 
# a.next.next.next.next = ListNode(5)
# 
# a.next == a.next.next.next
# Out[32]: False
#==============================================================================
