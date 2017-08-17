#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:35:23 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        value = 0
        while node is not None:
            value = value * 10 + node.val
            node = node.next
        value += 1
        node = ListNode(value % 10)
        value = value // 10
        while value != 0:
            temp = ListNode(value % 10)
            temp.next = node
            node = temp
            value = value // 10
        return node
    
s = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
result = s.plusOne(node)
            
        