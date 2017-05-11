#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 23:19:18 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # linked list的套路
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        result1 = ListNode(0)
        temp1 = result1
        result2 = ListNode(0)
        temp2 = result2
        while head is not None:
            value = head.val
            if value < x:
                temp1.next = ListNode(value)
                temp1 = temp1.next
            else:
                temp2.next = ListNode(value)
                temp2 = temp2.next
            head = head.next
        temp1.next = result2.next
        return result1.next
#==============================================================================
#     def partition(self, head, x):
#         # 这样是不行的，要按照上面那个才行
#         """
#         :type head: ListNode
#         :type x: int
#         :rtype: ListNode
#         """
#         result1 = ListNode(0)
#         temp1 = result1.next
#         result2 = ListNode(0)
#         temp2 = result2.next
#         while head is not None:
#             value = head.val
#             if value < x:
#                 temp1 = ListNode(value)
#                 temp1 = temp1.next
#             else:
#                 temp2 = ListNode(value)
#                 temp2 = temp2.next
#             head = head.next
#         temp1 = result2.next
#         return result1.next
#==============================================================================
