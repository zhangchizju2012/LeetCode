#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:09:20 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        tempA = headA
        tempB = headB
        label = True
        while tempA.val != tempB.val:
            if tempA.next is not None:
                tempA = tempA.next
            elif label == True:
                tempA = headB
                label = False
            else:
                return None
            if tempB.next is not None:
                tempB = tempB.next
            else:
                tempB = headA
        return tempA
b = ListNode(4)
b.next = ListNode(5)
b.next.next = ListNode(6)
a = ListNode(7)
s = Solution()
print s.getIntersectionNode(a,b)
#==============================================================================
# a = ListNode(3)
# a.next = ListNode(4)
# a.next.next = ListNode(5)
# 
# a.val
# Out[14]: 3
# 
# a.next.val
# Out[15]: 4
# 
# a.next.next.val
# Out[16]: 5
# 
# b = a
# b = b.next #b挪到下一个不会影响a
# 
# b.val
# Out[19]: 4
# 
# a.val
# Out[20]: 3
#==============================================================================
