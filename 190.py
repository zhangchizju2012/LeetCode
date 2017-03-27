#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 23:04:24 2017

@author: zhangchi
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binaryList = []
        while n!=0:
            binaryList.append(n%2)
            n=n//2
        while len(binaryList)<32:
            binaryList.append(0)
        weight = 1
        result = 0
        for i in range(len(binaryList)-1,-1,-1):
            result += weight * binaryList[i]
            weight *= 2
        return result
        
s = Solution()
print s.reverseBits(43261596)