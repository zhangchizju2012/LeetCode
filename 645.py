#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:26:21 2017

@author: zhangchi
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = set()
        length = len(nums)
        for i in xrange(1,length+1):
            temp.add(i)
        result = []
        for item in nums:
            if item in temp:
                temp.remove(item)
            else:
                result.append(item)
        result.append(temp.pop())
        return result
s = Solution()
print s.findErrorNums([1,1])