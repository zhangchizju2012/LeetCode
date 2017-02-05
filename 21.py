#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:17:02 2016

@author: zhangchi
"""

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is not None and l2 is not None:
            l = ListNode(min(l1.val,l2.val))
            temp = l
            if l1.val == min(l1.val,l2.val):
                l1 = l1.next
            else:
                l2 = l2.next
        else:
            if l1 is None:
                return l2
            else:
                return l1
        while l1 is not None and l2 is not None:
            temp.next = ListNode(min(l1.val,l2.val))
            if l1.val == min(l1.val,l2.val):
                l1 = l1.next
            else:
                l2 = l2.next
            temp = temp.next
        if l1 is None:
            temp.next = l2
        else:
            temp.next = l1
        return l