#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:32:38 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
            
        temp_1 = head
        count = 0
        while temp_1 is not None:
            count = count + 1
            temp_1 = temp_1.next
        k = k%count
        #不如遍历所有数，把数都取出来，然后再构建链表
        
        save = ListNode(0)
        save.next = head
        result = ListNode(0)
        temp = save
        result_temp = result
        for i in range(k):
            head = head.next#是否可以不产生save,对save的操作直接对head进行
        while head is not None:
            head = head.next
            result_temp.next = ListNode(temp.next.val)
            temp = temp.next
            result_temp = result_temp.next
        a = ListNode(0)
        temp_a = a
        while temp.next is not None:
            temp_a.next = ListNode(temp.next.val)
            temp_a = temp_a.next
            temp = temp.next
        temp_a.next = result.next
        return a.next