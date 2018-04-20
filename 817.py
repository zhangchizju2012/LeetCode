#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 17:11:00 2018

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        count = 0
        label = False
        check = set()
        for item in G:
            check.add(item)
        while head is not None:
            if label is False:
                if head.val in check:
                    label = True
                    count += 1
            else:
                if head.val not in check:
                    label = False
            head = head.next
            
        return count
    
node = ListNode(0)
node.next = ListNode(1)
node.next.next = ListNode(2)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(4)

s = Solution()
print(s.numComponents(node,[0, 3, 1, 4]))
