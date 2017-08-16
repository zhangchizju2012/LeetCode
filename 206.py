#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:58:34 2017

@author: zhangchi
"""

"""
Reviewed on Wed Aug 16 12:33:50 2017

@author: zhangchi
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    # recursion 版本，其实还是开始那个直接来的版本好
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is not None:
            result, _ = self.helper(head)
            return result
    
    def helper(self, node):
        if node.next is not None:
            previous, temp = self.helper(node.next)
            newNode = ListNode(node.val)
            temp.next = newNode
            return previous, newNode # newNode是尾部node的指针，这个还挺有用的，避免之后重复扫描
        else:
            return node, node
        
class Solution(object):
    # recursion 版本 慢速
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is not None:
            return self.helper(head)
    
    def helper(self, node):
        if node.next is not None:
            previous = self.helper(node.next)
            temp = previous
            while temp.next is not None: # 这里很多都是重复了的
                temp = temp.next
            temp.next = ListNode(node.val)
            return previous
        else:
            return node

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        now = ListNode(head.val)
        prev = None
        while head.next is not None: # 直接来
            head = head.next
            prev = now
            now = ListNode(head.val)
            now.next = prev
        return now