#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 19:27:12 2017

@author: zhangchi
"""

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return
        dictionary = {}
        dictionary[node.label] = UndirectedGraphNode(node.label)
        nodeList = [node]
        import Queue
        temp = Queue.Queue()
        temp.put(node)
        while temp.empty() is False:
            tempNode = temp.get()
            for item in tempNode.neighbors:
                if item.label not in dictionary:
                    dictionary[item.label] = UndirectedGraphNode(item.label)
                    nodeList.append(item)
                    temp.put(item)
        for node in nodeList:
            for neigh in node.neighbors:
                dictionary[node.label].neighbors.append(dictionary[neigh.label])
        return dictionary[nodeList[0].label]
        
a = UndirectedGraphNode(0)
b = UndirectedGraphNode(1)
c = UndirectedGraphNode(2)
a.neighbors.append(b)
a.neighbors.append(c)
b.neighbors.append(a)
b.neighbors.append(c)
c.neighbors.append(a)
c.neighbors.append(b)
c.neighbors.append(c)
s = Solution()
d = s.cloneGraph(a)