#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 07:12:04 2017

@author: zhangchi
"""

class Solution(object):
    def __init__(self):
        self.result = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.helper(n, [])
        finalResult = []
        for item in self.result:
            if self.checkValid(item) == True:
                finalResult.append(self.changeStyle(item,n))
        return finalResult
    
    def helper(self, n, alist):
        if len(alist) == n:
            self.result.append(alist)
        else:
            for i in range(n):
                if self.checkValid(alist):
                    if i not in alist:
                        self.helper(n, alist+[i])
                else:
                    break
            
    def checkValid(self, alist):
        temp = []
        for i, j in enumerate(alist):
            if (i+j) not in temp:
                temp.append(i+j)
            else:
                return False
        temp = []
        for i, j in enumerate(alist):
            if (i-j) not in temp:
                temp.append(i-j)
            else:
                return False
        return True
        
    def changeStyle(self, alist, n):
        temp = []
        for item in alist:
            temp.append('.'*item+'Q'+'.'*(n-item-1))
        return temp
        
#==============================================================================
# class Solution(object):
#     def __init__(self):
#         self.result = []
# 
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#         self.helper(n, [])
#         finalResult = []
#         for item in self.result:
#             if self.checkValid(item) == True:
#                 finalResult.append(self.changeStyle(item,n))
#         return finalResult
#     
#     def helper(self, n, alist):
#         if len(alist) == n:
#             self.result.append(alist)
#         else:
#             for i in range(n):
#                 if i not in alist:
#                     self.helper(n, alist+[i])
#             
#     def checkValid(self, alist):
#         temp = []
#         for i, j in enumerate(alist):
#             if (i+j) not in temp:
#                 temp.append(i+j)
#             else:
#                 return False
#         temp = []
#         for i, j in enumerate(alist):
#             if (i-j) not in temp:
#                 temp.append(i-j)
#             else:
#                 return False
#         return True
#         
#     def changeStyle(self, alist, n):
#         temp = []
#         for item in alist:
#             temp.append('.'*item+'Q'+'.'*(n-item-1))
#         return temp
#==============================================================================
                    
s = Solution()
print s.solveNQueens(9)