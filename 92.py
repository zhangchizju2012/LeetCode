#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:44:49 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        now = head
        previous = None
        count = 1
        while count < m:
            count += 1
            previous = now
            now = now.next
        node = ListNode(now.val)
        last = node
        while count < n:
            now = now.next
            newNode = ListNode(now.val)
            newNode.next = node
            node = newNode
            count += 1
        if previous is not None:# m!=1
            previous.next = node
            last.next = now.next
            return head
        else:# m==1
            last.next = now.next
            if n == 1: # m==1且n==1的情况
                return head
            else:
                return newNode