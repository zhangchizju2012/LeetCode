#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:06:16 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        value1 = 0
        while l1 is not None:
            value1 = value1 * 10 + l1.val
            l1 = l1.next
        value2 = 0
        while l2 is not None:
            value2 = value2 * 10 + l2.val
            l2 = l2.next
        value = value1 + value2
        node = ListNode(value % 10)
        value = value // 10
        temp = node
        while value != 0:
            node = ListNode(value % 10)
            node.next = temp
            temp = node
            value = value // 10
        return temp
        