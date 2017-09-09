#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:06:01 2017

@author: zhangchi
"""

# 看了答案：https://discuss.leetcode.com/topic/34701/java-easy-version-to-understand
# 自己写的
# 核心思路：哈希表把node的位置记住（其他信息可以放在node里），然后利用doublelinkedlist就可以轻松删除node
# 包括ddl可以轻松在头尾出增删节点

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.end = None

class Node(object):
    def __init__(self, value, key = None):
        self.value = value
        self.key = key
        self.pre = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.dic = {}
        self.dl = DoubleLinkedList()
        self.dl.head = Node('start') # 为了避免add, delete时对开头结尾的各种异常处理
        self.dl.end = Node('end')
        self.dl.head.next = self.dl.end
        self.dl.end.pre = self.dl.head
        
    def deleteNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.count -= 1
        
    def addNode(self, newNode):
        self.dl.head.next.pre = newNode
        newNode.next = self.dl.head.next
        newNode.pre = self.dl.head
        self.dl.head.next = newNode
        self.count += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            value = node.value
            self.deleteNode(node)
            self.addNode(node)
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic: # 更新值的情况
            node = self.dic[key]
            self.deleteNode(node)
            newNode = Node(value,key)
            self.addNode(newNode)
            self.dic[key] = newNode
        else:
            node = Node(value,key)
            self.dic[key] = node
            self.addNode(node)
            if self.count > self.capacity: # 一律先加了，多了再处理
                self.dic.pop(self.dl.end.pre.key)
                self.deleteNode(self.dl.end.pre)
            