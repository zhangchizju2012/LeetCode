#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:21:36 2017

@author: zhangchi
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # version 1: a little bit slow
        '''
        d = [0 for i in range(32)]
        for item in nums:
            for i in range(32):
                if (1<<i) & item > 0:
                    d[i] += 1
        position = None
        for i in range(32):
            if d[i]%2 == 1:
                position = i
                break
        '''
        # version 2
        tempResult = 0
        for item in nums:
            tempResult ^= item
        position = 0
        while tempResult != 0:
            if tempResult %2 == 1:
                break
            else:
                tempResult = tempResult // 2
                position += 1
        # the following is the same
        firstResult = 0
        secondResult = 0
        for item in nums:
            if (1<<position) & item > 0:
                firstResult ^= item
            else:
                secondResult ^= item
        return [firstResult,secondResult]
s= Solution()
print s.singleNumber([1, 2, 1, 3, 2, 5])