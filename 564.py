#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:56:33 2017

@author: zhangchi
"""
#==============================================================================
# 564. Find the Closest Palindrome Add to List
# 
# Given an integer n, find the closest integer (not including itself), which is a palindrome.
# 
# The 'closest' is defined as absolute difference minimized between two integers.
# 
# Example 1:
# Input: "123"
# Output: "121"
# Note:
# The input n is a positive integer represented by string, whose length will not exceed 18.
# If there is a tie, return the smaller one as answer.
# Subscribe to see which companies asked this question.
#==============================================================================


class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        candidate = []
        if length % 2 == 1:
            before = length // 2 + 1
            beforeNumber = int(n[:before])
            temp1 = str(beforeNumber+1)#[-1*before:]
            temp2 = str(beforeNumber)
            temp3 = str(beforeNumber-1)
            candidate.append(int(temp1+temp1[:-1][::-1]))
            candidate.append(int(temp2+temp2[:-1][::-1]))
            candidate.append(int(temp3+temp3[:-1][::-1]))
        else:
            before = length // 2
            beforeNumber = int(n[:before])
            temp1 = str(beforeNumber+1)#[-1*before:]
            temp2 = str(beforeNumber)
            temp3 = str(beforeNumber-1)
            candidate.append(int(temp1+temp1[::-1]))
            candidate.append(int(temp2+temp2[::-1]))
            candidate.append(int(temp3+temp3[::-1]))
        if length > 1:
            candidate.append(int("9"*(length-1)))
        candidate.append(int("1"+"0"*(length-1)+"1"))
        candidate.sort()
        diff = float('inf')
        result = None
        for item in candidate:
            if abs(item - int(n)) < diff and item != int(n):
                result = item
                diff = abs(item - int(n))
        return str(result)
        
#==============================================================================
# Python, Simple with Explanation
# Let's build a list of candidate answers for which the final answer must be 
# one of those candidates. Afterwards, choosing from these candidates is straightforward.
# 
# If the final answer has the same number of digits as the input string S, 
# then the answer must be the middle digits + (-1, 0, or 1) flipped into a 
# palindrome. For example, 23456 had middle part 234, and 233, 234, 235 flipped 
# into a palindrome yields 23332, 23432, 23532. Given that we know the number 
# of digits, the prefix 235 (for example) uniquely determines the corresponding 
# palindrome 23532, so all palindromes with larger prefix like 23732 are strictly 
# farther away from S than 23532 >= S.
# 
# If the final answer has a different number of digits, it must be of the form 
# 999....999 or 1000...0001, as any palindrome smaller than 99....99 or bigger 
# than 100....001 will be farther away from S.
# 
# def nearestPalindromic(self, S):
#     K = len(S)
#     candidates = [str(10**k + d) for k in (K-1, K) for d in (-1, 1)]
#     prefix = S[:(K+1)/2]
#     P = int(prefix)
#     for start in map(str, (P-1, P, P+1)):
#         candidates.append(start + (start[:-1] if K%2 else start)[::-1])
#     
#     def delta(x):
#         return abs(int(S) - int(x))
#     
#     ans = None
#     for cand in candidates:
#         if cand != S and not cand.startswith('00'):
#             if (ans is None or delta(cand) < delta(ans) or
#                     delta(cand) == delta(ans) and int(cand) < int(ans)):
#                 ans = cand
#     return ans
#==============================================================================
