#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:48:47 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        count = 0
        point = root
        while point is not None:
            count += 1
            point = point.next
            
        average = count // k
        left = count % k
        total = [average] * k
        for i in xrange(left):
            total[i] += 1
            
        result = []
        
        for item in total:
            value = item
# =============================================================================
#             if value == 0:
#                 result.append(None)
#             else:
# =============================================================================
            node = ListNode(0)
            temp = node
            while value > 0:
                temp.next = ListNode(root.val)
                temp = temp.next
                root = root.next
                value -= 1
            result.append(node.next)
        return result
                
    
s = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
temp = s.splitListToParts(node,6)