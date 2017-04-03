#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:43:02 2017

@author: zhangchi
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        string = []
        prev = None
        result = []
        for item in nums:
            if string == []:
                string = [item]
                prev = item
            elif prev + 1 < item:
                if string[0] != prev:
                    string.append(prev)
                result.append(string)
                string = [item]
                prev = item
            else:
                prev = item
        if string[0] != prev:
            string.append(prev)
        result.append(string)
        
        finalResult = []
        for item in result:
            if len(item) == 2:
                finalResult.append(str(item[0])+'->'+str(item[1]))
            else:
                finalResult.append(str(item[0]))
        return finalResult
        
s = Solution()
print s.summaryRanges([0,1,2,4,7,8,13,14,15])