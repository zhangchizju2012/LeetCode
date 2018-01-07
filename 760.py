#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:32:26 2018

@author: zhangchi
"""

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = {}
        for index, item in enumerate(B):
            if item not in dic:
                dic[item] = [index]
            else:
                dic[item].append(index)
                
        result = []
        for item in A:
            result.append(dic[item].pop())
        return result
    
s = Solution()
print s.anagramMappings([12, 28, 46, 32, 50],[50, 12, 32, 46, 28])