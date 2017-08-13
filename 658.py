#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:34:43 2017

@author: zhangchi
"""

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        dic = {}
        for item in arr:
            dif = abs(item - x)
            if dif not in dic:
                dic[dif] = [item]
            else:
                dic[dif].append(item)
        difList = dic.keys()
        difList.sort()
        result = []
        for item in difList:
            length = len(dic[item])
            if length <= k:
                k -= length
                result += dic[item]
                if k == 0:
                    result.sort()
                    return result
            else:
                result += dic[item][:k]
                result.sort()
                return result
            
s = Solution()
print s.findClosestElements([1], 1, 1)