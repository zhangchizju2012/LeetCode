#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 23:05:36 2017

@author: zhangchi
"""

import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        result = ListNode(0)
        temp = result
        for item in lists:
            if item is not None:
                heapq.heappush(heap,(item.val,item.next))
        while len(heap) > 0:
            value, node = heapq.heappop(heap)
            temp.next = ListNode(value)
            temp = temp.next
            if node is not None:
                heapq.heappush(heap,(node.val,node.next))
        return result.next
        
    # review, comparing these two to understand linked list
    # the following version does not work
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        result = ListNode(0)
        temp = result.next # not ok
        for item in lists:
            if item is not None:
                heapq.heappush(heap,(item.val,item.next))
        while len(heap) > 0:
            value, node = heapq.heappop(heap)
            temp = ListNode(value) # not ok
            temp = temp.next
            if node is not None:
                heapq.heappush(heap,(item.val,item.next))
        return result.next