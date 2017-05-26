#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 22:52:19 2017

@author: zhangchi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
#==============================================================================
#     注意linked list的套路
#     笔记里有一张截图
#     a = ListNode(1)
#     a.next = ListNode(2)
#     a.next.val
#     Out[4]: 2
#     b=a
#     b=b.next
#     a.next.val
#     Out[7]: 2
#     注意以上这种方式不改变a.next.val（b只是一个引用，b=b.next意味着改变了b引用的对象，所以不影响a.next.val的值）
#     a.val
#     Out[8]: 1
#     a = ListNode(1)
#     d = ListNode(4)
#     a.next = ListNode(2)
#     b=a
#     b.next = d
#     a.next.val
#     Out[14]: 4
#     注意此处a.next.val的值发生了改变，b还是一个引用，但b=a意味着b引用的对象和a引用的对象相同，b.next=d导致a引用的对象也发生了改变
#     （.next有点像按了遥控器（Java书里的类比）），所以a.next.val值发生改变
#==============================================================================
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        slist = []
        temp = head
        while temp is not None:
            slist.append(temp)
            temp = temp.next
        length = len(slist)
        count = (length - 1) // 2
        temp = head
        while count > 0:
            point = slist.pop()
            point.next = temp.next
            temp.next = point
            temp = temp.next.next
            count -= 1
        if length > 0:
            if length % 2 == 1:
                temp.next = None
            else:
                temp.next.next = None