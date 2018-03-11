#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:39:09 2018

@author: zhangchi
"""

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.data = graph
        self.hashtable = {}
        self.dic = {}
        for index, nodes in enumerate(graph):
            for node in nodes:
                if node not in self.dic:
                    self.dic[node] = [index]
                else:
                    self.dic[node].append(index)
        # print(self.dic)       
        return self.helper(len(graph)-1)
        
    def helper(self, n):
        if n == 0:
            return [[0]]
        else:
            if n not in self.hashtable:
                result = []
                for node in self.dic[n]:
                    for temp in self.helper(node):
                        result.append(temp+[n])
                self.hashtable[n] = result
            return self.hashtable[n]


s = Solution()
print(s.allPathsSourceTarget([[1,2], [3], [3], []] ))