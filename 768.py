#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 20:39:42 2018

@author: zhangchi
"""

class Solution(object):
    # 先转变成769.py
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        after = sorted(arr)
        dic = {}
        for index, item in enumerate(after):
            if item not in dic:
                dic[item] = index
        for i in xrange(len(arr)):
            value = dic[arr[i]]
            dic[arr[i]] += 1
            arr[i] = value
            #after[i] = dic[after[i]]
        
        #print arr
        #print after
        
        maxValue = arr[0]
        count = 0
        for i in xrange(len(arr)):
            if arr[i] > maxValue:
                maxValue = arr[i]
            arr[i] = maxValue
        for i in xrange(len(arr)):
            if i == arr[i]:
                count += 1
        return count
        
s = Solution()
print s.maxChunksToSorted([1,1,0,0,1])