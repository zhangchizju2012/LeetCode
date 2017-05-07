#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 10:39:21 2017

@author: zhangchi
"""

class Solution(object):
    # DP, 想想能不能不用recrusion的方式
    def __init__(self):
        self.dic = {}
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        self.m = m
        self.n = n
        return self.helper(i,j,N)
        
    def helper(self,i,j,n):
        if i == -1 or j == -1 or i == self.m or j == self.n: # 加上这个可以避免最后一个else里出现大量的if,else
            return 1
        elif n < 1:
            return 0
        elif (i,j,n) in self.dic:
            return self.dic[(i,j,n)]
        else:
            temp = self.helper(i-1,j,n-1) + self.helper(i+1,j,n-1) + self.helper(i,j-1,n-1) + self.helper(i,j+1,n-1)
            self.dic[(i,j,n)] = temp % (10 ** 9 + 7)
            return self.dic[(i,j,n)]
s = Solution()
print s.findPaths(50,50,50,0,0)

#==============================================================================
# class Solution(object):
#     # it also works
#     def __init__(self):
#         self.dic = {}
#     def findPaths(self, m, n, N, i, j):
#         """
#         :type m: int
#         :type n: int
#         :type N: int
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         #这里看起来没有必要
#         for k in range(m):
#             self.dic[(k,0,1)] = 0
#             self.dic[(k,n-1,1)] = 0
#         for k in range(n):
#             self.dic[(0,k,1)] = 0
#             self.dic[(m-1,k,1)] = 0
#         for k in range(m):
#             self.dic[(k,0,1)] += 1
#             self.dic[(k,n-1,1)] += 1
#         for k in range(n):
#             self.dic[(0,k,1)] += 1
#             self.dic[(m-1,k,1)] += 1
#         self.m = m
#         self.n = n
#         return self.helper(i,j,N)
#         
#     def helper(self,i,j,n):
#         if n < 1:
#             return 0
#         elif i == -1 or j == -1 or i == self.m or j == self.n:
#             return 1
#         elif (i,j,n) in self.dic:
#             return self.dic[(i,j,n)]
#         else:
#             temp = self.helper(i-1,j,n-1) + self.helper(i+1,j,n-1) + self.helper(i,j-1,n-1) + self.helper(i,j+1,n-1)
#             self.dic[(i,j,n)] = temp % (10 ** 9 + 7)
#             return self.dic[(i,j,n)]
#==============================================================================
