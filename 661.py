#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 19:29:34 2017

@author: zhangchi
"""

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        length = len(M[0])
        result = []
        dic = {}
        for i in xrange(row):
            for j in xrange(length):
                dic[(i,j)] = [M[i][j],1]
        for i in xrange(-1,length+1):
            dic[(-1,i)] = [0,0]
            dic[(row,i)] = [0,0]
        for i in xrange(-1,row+1):
            dic[(i,-1)] = [0,0]
            dic[(i,length)] = [0,0]
        for i in xrange(row):
            temp = []
            for j in xrange(length):
                value = dic[(i-1,j-1)][0] + dic[(i-1,j)][0] + dic[(i-1,j+1)][0] + dic[(i,j-1)][0] + dic[(i,j)][0] + dic[(i,j+1)][0] + dic[(i+1,j-1)][0] + dic[(i+1,j)][0] + dic[(i+1,j+1)][0]
                number = dic[(i-1,j-1)][1] + dic[(i-1,j)][1] + dic[(i-1,j+1)][1] + dic[(i,j-1)][1] + dic[(i,j)][1] + dic[(i,j+1)][1] + dic[(i+1,j-1)][1] + dic[(i+1,j)][1] + dic[(i+1,j+1)][1]
                temp.append(value/number)
            result.append(temp)
        return result
    
s = Solution()
a = [[1,1,1]]
print s.imageSmoother(a)
                