#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:14:11 2017

@author: zhangchi
"""

class Solution(object):
    # topological sort
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        temp = {}
        row = len(matrix)
        if row == 0:
            return 0
        lenght= len(matrix[0])
        if lenght == 0:
            return 0
        # 方便查询，并且延伸一层，避免之后大量的if else
        for i in xrange(row):
            for j in xrange(lenght):
                temp[(i,j)] = matrix[i][j]
        # 延伸一层并置为X，避免之后大量的if else
        for i in xrange(-1,row+1):
            temp[(i,-1)] = float('inf')
            temp[(i,lenght)] = float('inf')
        for i in xrange(lenght):
            temp[(-1,i)] = float('inf')
            temp[(row,i)] = float('inf')
        
        from Queue import Queue
        q = Queue()
        dic = {}
        # 找到局部最小点
        for i in xrange(row):
            for j in xrange(lenght):
                if temp[(i,j)] <= min(temp[(i-1,j)],temp[(i+1,j)],temp[(i,j-1)],temp[(i,j+1)]):
                    q.put((i,j))
                    dic[(i,j)] = 1
        # topological sort
        while q.empty() is False:
            (a,b) = q.get()
            value = temp[(a,b)]
            count = dic[(a,b)]
            if temp[(a-1,b)] > value and temp[(a-1,b)] != float('inf'):
                dic[(a-1,b)] = count + 1
                q.put((a-1,b))
            if temp[(a+1,b)] > value and temp[(a+1,b)] != float('inf'):
                dic[(a+1,b)] = count + 1
                q.put((a+1,b))
            if temp[(a,b-1)] > value and temp[(a,b-1)] != float('inf'):
                dic[(a,b-1)] = count + 1
                q.put((a,b-1))
            if temp[(a,b+1)] > value and temp[(a,b+1)] != float('inf'):
                dic[(a,b+1)] = count + 1
                q.put((a,b+1))
        return count
        
s = Solution()
#print s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
print s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])
        