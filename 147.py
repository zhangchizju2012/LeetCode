#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:43:57 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.result = None
    
    def insert(self,value):
        node = ListNode(value)
        if self.result is None:
            self.result = node
        elif value <= self.result.val:
            node.next = self.result
            self.result = node
        else:
            head = self.result
            previous = None
            while head is not None and head.val <= value:
                previous = head
                head = head.next
            if head is None:
                previous.next = node
            else:
                previous.next = node
                node.next = head
            
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        while temp is not None:
            self.insert(temp.val)
            temp = temp.next
        return self.result
        
        