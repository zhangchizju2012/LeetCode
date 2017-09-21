#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:58:30 2017

@author: zhangchi
"""

# 0920复习

# 感觉是bfs/dfs？ 有点分不清了。应该是dfs
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.result = []
        self.helper(0,0,'')
        return self.result
        
    def helper(self, left, right, temp):
        if right == self.n:
            self.result.append(temp)
        else:
            if left < self.n:
                self.helper(left+1, right, temp+'(')
            if right < left:
                self.helper(left, right+1, temp+')')
                
s = Solution()
print s.generateParenthesis(6)
            
# =============================================================================
# # 复习时重写的版本
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         self.result = []
#         self.helper(0,"",n)
#         return self.result
#         
#     def helper(self,stack, previous, n): # stack相等于(和)的个数差值，跟之前的其实差不多
#         if stack > 0:
#             if n > 0:
#                 self.helper(stack+1, previous+'(', n-1)
#                 self.helper(stack-1, previous+')', n)
#             else:
#                 self.helper(stack-1, previous+')', n)
#         else:
#             if n > 0:
#                 self.helper(stack+1, previous+'(', n-1)
#             else:
#                 self.result.append(previous)
# 
# """
# Created on Mon May  8 22:32:39 2017
# 
# @author: zhangchi
# """
# 
# class Solution(object):
#     def __init__(self):
#         self.result = []
# 
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         self.length = 2 * n
#         self.helper("",n,n)
#         return self.result
#     
#     def helper(self,string,plus,minus):
#         if self.length == len(string):
#             self.result.append(string)
#         else:
#             if plus == minus:
#                 # “("一定要比"）"多
#                 self.helper(string+"(",plus-1,minus)
#             else:
#                 if plus >= 1:
#                     self.helper(string+"(",plus-1,minus)
#                 if minus >= 1:
#                     self.helper(string+")",plus,minus-1)
# s = Solution()
# print s.generateParenthesis(6)
# =============================================================================
