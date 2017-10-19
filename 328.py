#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 12:12:21 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 回顾143.py
    # 注意只要不是基础数据结构 都是引用！用引用的观点去思考 很好理解
    # 这些a,b,d其实全都是遥控器，a=xx这种形式只是改变引用的对象，而不会对原来引用的对象有任何的影响，a.xx=这种形式才能改变原来引用对象
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(0)
        tempOdd = odd
        even = ListNode(0)
        tempEven = even
        count = 0
        while head is not None:
            if count%2 == 0:
                tempOdd.next = head
                tempOdd = tempOdd.next
            else:
                tempEven.next = head
                tempEven = tempEven.next
            count += 1
            head = head.next
        tempEven.next = None
        tempOdd.next = even.next
        return odd.next
        
    # 改进的方向：https://discuss.leetcode.com/topic/34292/simple-o-n-time-o-1-space-java-solution
    # 在linked list内部操作，最后连起来
    
        
n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
s = Solution()
result = s.oddEvenList(n)