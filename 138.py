#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:26:16 2017

@author: zhangchi
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node = RandomListNode(0)
        start = node
        temp = head
        dic = {}
        dic1 = {None:None}
        while temp is not None:
            node.next = RandomListNode(temp.label)
            dic1[temp] = node.next # 两个linkedlist的各个节点对应起来
            if temp.random not in dic: # 把原来的linkedlist的random对象和父对象对应起来放在dic里
                dic[temp.random] = [temp]
            else:
                dic[temp.random].append(temp)
            temp = temp.next
            node = node.next
        for node in dic: # 原linkedlist的random对象和父对象对应关系转移到新的linkedlist里
            for item in dic[node]:
                dic1[item].random = dic1[node]
        return start.next
            
        