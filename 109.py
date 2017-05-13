#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:47:01 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        return self.helper(nums)
            
    def helper(self,nums):
        length = len(nums)
        if length == 0:
            return None
        else:
            middle = length // 2
            node = TreeNode(nums[middle])
            left = self.helper(nums[:middle])
            right = self.helper(nums[middle+1:])
            node.left = left
            node.right = right
            return node
        
point = ListNode(1)
point.next = ListNode(2)
point.next.next = ListNode(3)
point.next.next.next = ListNode(4)
point.next.next.next.next = ListNode(5)
point.next.next.next.next.next = ListNode(6)
s = Solution()
result = s.sortedListToBST(point)