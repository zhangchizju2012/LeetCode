#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 09:27:43 2017

@author: zhangchi
"""

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        dic = {}
        for item in candies:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
#==============================================================================
#         check = {}
#         for item in dic:
#             if dic[item] in check:
#                 check[dic[item]] += 1
#             else:
#                 check[dic[item]] = 1
#==============================================================================
        total = len(candies)/2
        if len(dic) >= total:
            return total
        else:
            return len(dic)
        


s = Solution()
print s.distributeCandies([1,1,2,3])
