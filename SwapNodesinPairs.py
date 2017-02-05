#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:58:04 2016

@author: zhangchi
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        temp = result
        i = 0
        while head is not None and head.next is not None:
            if i == 0:
                temp.next = ListNode(head.next.val)
                i = 1
            else:
                temp.next = ListNode(head.val)
                i = 0
                head = head.next.next
            temp = temp.next
        if head is not None:
            temp.next = ListNode(head.val)
        return result.next
        
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
S = Solution()
result = S.swapPairs(a)