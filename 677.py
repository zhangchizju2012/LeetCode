#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:43:04 2017

@author: zhangchi
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.num = 0
        self.children = []
        self.childrenValue = {} # key是字符，value是在self.children中所处的位置

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode("")
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        for item in key:
            if item in node.childrenValue:
                node = node.children[node.childrenValue[item]]
            else:
                newNode = TreeNode(item)
                node.childrenValue[item] = len(node.children)
                node.children.append(newNode)
                node = newNode
        if "" not in node.childrenValue:
            newNode = TreeNode("") # 用来表示一个string的结束
            newNode.num = val
            node.childrenValue[""] = len(node.children)
            node.children.append(newNode)
        else:
            node = node.children[node.childrenValue[""]]
            node.num = val
        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        result = 0
        node = self.root
        for item in prefix:
            if item in node.childrenValue:
                node = node.children[node.childrenValue[item]]
            else:
                return result
        childrenList = [node]
        temp = []
        while len(childrenList) > 0:
            for item in childrenList:
                result += item.num
                temp += item.children
            childrenList = temp
            temp = []
        return result
    
s = MapSum()
print s.insert("apple", 3)
#print s.insert("apple", 4)
print s.sum("ap")
print s.insert("app", 2)
print s.sum("appe")

        