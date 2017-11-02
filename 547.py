#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:16:45 2017

@author: zhangchi
"""

class Solution(object):
    # bfs
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        length = len(M)
        dic = {}
        for i in xrange(length):
            dic[i] = set()
        
        for i in xrange(length):
            for j in xrange(i+1,length):
                if M[i][j] == 1:
                    dic[i].add(j)
                    dic[j].add(i)
        
        count = 0
        removeSet = set()
        for item in dic:
            if len(dic[item]) == 0:
                removeSet.add(item)
        count += len(removeSet)
        for item in removeSet:
            dic.pop(item)
            
        while len(dic) > 0:
            removeSet = set()
            startNode = dic.keys()[0]
            removeSet.add(startNode)
            nowList = [startNode]
            while len(nowList) > 0:
                future = []
                for now in nowList:
                    for item in dic[now]:
                        if item not in removeSet:
                            future.append(item)
                            removeSet.add(item)
                nowList = future
            count += 1
            for item in removeSet:
                dic.pop(item)
            
        return count
    
s = Solution()
a = [[1]]
print s.findCircleNum(a)