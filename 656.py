#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:18:37 2017

@author: zhangchi
"""

class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        self.dic = {1:(A[0],[1])}
        for index, item in enumerate(A):
            if item == -1:
                self.dic[index+1] = (float('inf'),[])
        self.a = A
        self.b = B
        cost, path = self.helper(len(A))
        if cost == float('inf'):
            return []
        else:
            return path
        
    def helper(self, n):
        if n not in self.dic:
            cost = float('inf')
            path = []
            for i in xrange(n-1,max(0,n-self.b-1),-1):
                tempCost, tempPath = self.helper(i)
                if tempCost < cost:
                    cost = tempCost
                    path = tempPath + [n]
                elif tempCost == cost:
                    path = self.comparePath(path, tempPath+[n])
            self.dic[n] = (cost+self.a[n-1],path)
        return self.dic[n]
                    
                    
    def comparePath(self, a, b):
        for itemA, itemB in zip(a,b):
            if itemA < itemB:
                return a
            elif itemA > itemB:
                return b
        if len(a) > len(b):
            return b
        else:
            return a
            
s = Solution()
print s.cheapestJump([1,2,4,-1,2], 2)