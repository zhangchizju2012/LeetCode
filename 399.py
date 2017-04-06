#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:50:23 2017

@author: zhangchi
"""
import collections

class Solution(object):
    def calcEquation(self, equations, values, query):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type query: List[List[str]]
        :rtype: List[float]
        """
        # http://bookshadow.com/weblog/2016/09/11/leetcode-evaluate-division/
        g = collections.defaultdict(lambda: collections.defaultdict(int))
        for (s, t), v in zip(equations, values):
            g[s][t] = v
            g[t][s] = 1.0 / v
        for k in g:
            g[k][k] = 1.0
            for s in g:
                for t in g:
                    if g[s][k] and g[k][t]:
                        g[s][t] = g[s][k] * g[k][t]
        ans = []
        for s, t in query:
            ans.append(g[s][t] if g[s][t] else -1.0)
        return ans
                
        
    def calcEquation2(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
#==============================================================================
#         # has bug when 
#         [["a","b"],["e","f"],["b","e"]]
#         [3.4,1.4,2.3]
#         [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
#==============================================================================
        
        dictionary = {}
        for i in range(len(equations)):
            item = equations[i]
            first = item[0]
            second = item[1]
            if first in dictionary:
                dictionary[first][second] = values[i]
            else:
                dictionary[first] = {second:values[i]}
                if second in dictionary:
                    for thing in dictionary[second]:
                        dictionary[first][thing] = values[i] * dictionary[second][thing]
            if second in dictionary:
                dictionary[second][first] = 1./values[i]
            else:
                dictionary[second] = {first:1./values[i]}
                if first in dictionary:
                    for thing in dictionary[first]:
                        dictionary[second][thing] = 1./values[i] * dictionary[first][thing]
            for word in dictionary:
                if first in dictionary[word]:
                    dictionary[word][second] = dictionary[word][first] * values[i]
                if second in dictionary[word]:
                    dictionary[word][first] = dictionary[word][second] * (1./values[i])
                    
        result = []
        for item in queries:
            if item[0] in dictionary:
                if item[1] in dictionary[item[0]]:
                    result.append(dictionary[item[0]][item[1]])
                else:
                    result.append(-1)
            else:
                result.append(-1)
        return result
    
s = Solution()
a = [["a","b"],["e","f"],["b","e"]]
b = [3.4,1.4,2.3]
c = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
print s.calcEquation(a,b,c)