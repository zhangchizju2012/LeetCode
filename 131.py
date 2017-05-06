#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 21:15:49 2017

@author: zhangchi
"""

class Solution(object):
    # DP, use for loop instead of recursion
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return [[]]
        dic = {}
        length = len(s)
        for i in xrange(length+1):
            dic[i] = []
        dic[length].append([])
        # line22: for the case such as "ccaba", it will result in error in line 29 if no this line
        dic[length-1].append([s[-1]]) 
        for i in xrange(length-2,-1,-1):
            for j in xrange(i,length):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    for item in dic[j+1]:
                        dic[i].append([temp]+item)
        return dic[0]
                
        