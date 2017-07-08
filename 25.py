#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 01:15:40 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 粗粗地看了解法https://discuss.leetcode.com/topic/7126/short-but-recursive-java-code-with-comments
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while cur is not None and count < k:
            cur = cur.next
            count += 1
        if count == k:
            future = self.reverseKGroup(cur, k) # 后面的部分用recursion
            count = 0
            while count < k: # 调整前面k个node的顺序
                node = head
                head = head.next
                node.next = future
                future = node
                count += 1
            return future
        else: # 长度不够的话不用调整顺序
            return head
            
s = Solution()
print s.reverseKGroup()
            
#==============================================================================
#                 
#         
#     def helper(self, head):
#         # 翻转整个链表
#         result = None
#         while head is not None:
#             if result is None:
#                 result = head
#                 head = head.next
#                 result.next = None
#             else:
#                 node = head
#                 head = head.next
#                 node.next = result
#                 result = node
#         return result
#==============================================================================
