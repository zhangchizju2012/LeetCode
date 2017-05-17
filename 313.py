#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 23:48:29 2017

@author: zhangchi
"""

class Solution(object):
    # very similar to 264.py
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n <= 0:
            return None
        length = len(primes)
        indexList = [0] * length
        result = [1]
        valueList = [result[indexList[i]]*primes[i] for i in xrange(length)]
        while n > len(result):
            value = min(valueList)
            result.append(value)
            for i in xrange(length):
                if valueList[i] == value:
                    indexList[i] += 1
                    valueList[i] = result[indexList[i]]*primes[i]
        return result[-1]

s = Solution()
print s.nthSuperUglyNumber(12,[2, 7, 13, 19])