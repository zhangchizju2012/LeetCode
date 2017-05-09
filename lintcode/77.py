#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 22:48:14 2017
Edited on Sat May  9 10:13:15 2017

@author: zhangchi
"""

class Solution:
    # inspired by the video, dp2
    def __init__(self):
        self.result = {}
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        lengthA = len(A)
        lengthB = len(B)
        self.A = A
        self.B = B
        for i in xrange(lengthA+1):
            self.result[(i,0)] = 0
        for i in xrange(lengthB+1):
            self.result[(0,i)] = 0
        return self.helper(lengthA,lengthB)
        #self.result = [[-1]*le]
    def helper(self,i,j):
        if (i,j) not in self.result:
            if self.A[i-1] == self.B[j-1]:
                temp = self.helper(i-1,j-1) + 1
            else:
                temp = max(self.helper(i-1,j),self.helper(i,j-1))
            self.result[(i,j)] = temp
        return self.result[(i,j)]
                           
s = Solution()
print s.longestCommonSubsequence("ABCD", "EACB")
#==============================================================================
# class Solution:
#     """
#     @param A, B: Two strings.
#     @return: The length of longest common subsequence of A and B.
#     """
#     def longestCommonSubsequence(self, A, B):
#         # write your code here
#         dicA = {}
#         for i,item in enumerate(A):
#             if item in dicA:
#                 dicA[item].append(i)
#             else:
#                 dicA[item] = [i]
#         dicB = {}
#         for i,item in enumerate(B):
#             if item in dicB:
#                 dicB[item].append(i)
#             else:
#                 dicB[item] = [i]
#         length = len(A)
#         result = [[0]] * length
#         for i in range(length):
#             if A[i] in dicB:
#                 result[i] = [[dicB[A[i]][0]],[1]]
#                 for j in range(i):
#                     if len(A[j]) > 1:
#==============================================================================
                        
