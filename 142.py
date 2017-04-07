#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:40:03 2017

@author: zhangchi
"""
#==============================================================================
# |<---a---->|<--b-->|
# ###########&#######$##
#            #         #
#            #         #
#            #         #
#            #         #
#            ###########
# $ meeting point
# & the begin point of the circle
# circle size = c
# 2 ( a + b ) = a + nc + b
# so a = nc - b
# it means when a point starts from $, the other point starts from the beginning,
# the step of them are both 1, then they will meet at the begin point of the circle
#==============================================================================

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        pointA = head
        pointB = head
        label = False
        
        if pointA.next is not None:
                pointA = pointA.next
        else:
            return None
        if pointB.next is not None and pointB.next.next is not None:
            pointB = pointB.next.next
        else:
            return None
            
        while True:
            if pointA == pointB:
                label = True
                break
            if pointA.next is not None:
                pointA = pointA.next
            else:
                break
            if pointB.next is not None and pointB.next.next is not None:
                pointB = pointB.next.next
            else:
                break
        if label == False:
            return None
        else:
            pointC = head
            while pointC != pointB:
                pointC = pointC.next
                pointB = pointB.next
            return pointB