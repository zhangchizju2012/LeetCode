#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:32:42 2016

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 1
        l = ListNode(head.val)
        temp = l
        while head.next is not None:
            head = head.next
            temp.next = ListNode(head.val)
            length = length + 1
            temp = temp.next
        rank = length - n
        
        l_result = ListNode(0)
        temp = l_result
        count = 0
        while count != rank:
            temp.next  = ListNode(l.val)
            l = l.next
            count = count + 1
            temp = temp.next
        l = l.next
        temp.next = l
        return l_result.next
        
        '''
        jiuzhang 上的解法, much better.
    题意：删除链表中倒数第n个结点，尽量只扫描一遍。
    使用两个指针扫描，当第一个指针扫描到第N个结点后，
    第二个指针从表头与第一个指针同时向后移动，
    当第一个指针指向空节点时，另一个指针就指向倒数第n个结点了       
    
    def removeNthFromEnd(self, head, n):
        res = ListNode(0)
        res.next = head
        tmp = res
        for i in range(0, n):
            head = head.next
        while head != None:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        return res.next
        '''