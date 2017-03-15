#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 01:07:11 2017

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
        data = head.val
        label = True
        while head.next is not None:
            head = head.next
            if head.val != data and label == True:
                temp.next = ListNode(data)
                temp = temp.next
                data = head.val
            elif head.val != data and label != True:
                label = True
                data = head.val
            else:
                label = False
        if label == True:
            temp.next = ListNode(head.val)
        return result.next