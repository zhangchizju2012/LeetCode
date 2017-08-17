#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:34:03 2017

@author: zhangchi
"""

# =============================================================================
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# =============================================================================

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dic = {}
        node = head
        index = 0
        while node is not None:
            if node.val not in dic:
                dic[node.val] = set([index])
            else:
                dic[node.val].add(index)
            node = node.next
            index += 1
        index -= 1
        for item in dic:
            for value in dic[item]:
                if index - value not in dic[item]:
                    return False
        return True
    
s = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(1)
print s.isPalindrome(None)
            
        

