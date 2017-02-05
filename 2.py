#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:33:55 2016

@author: zhangchi
"""
"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
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
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        label = 0
        result = ListNode(0)
        temp = result
        while l1 is not None and l2 is not None:
            temp.next = ListNode((l1.val+l2.val+label)%10)
            label = (l1.val+l2.val+label)/10
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        if l1 is None and l2 is None:
            if label == 1:
                temp.next = ListNode(label)
        else:
            if l1 is None:
                while l2 is not None:
                    temp.next = ListNode((l2.val+label)%10)
                    label = (l2.val+label)/10
                    l2 = l2.next
                    temp = temp.next
            else:
                while l1 is not None:
                    temp.next = ListNode((l1.val+label)%10)
                    label = (l1.val+label)/10
                    l1 = l1.next
                    temp = temp.next
            if label == 1:
                temp.next = ListNode(label)
        return result.next
        
a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)
a.next.next.next = ListNode(1)
b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)
#b.next.next.next = ListNode(4)
S = Solution()
result = S.addTwoNumbers(a,b)
