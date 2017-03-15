#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:32:12 2017

@author: zhangchi
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return None
        indexA = 0
        indexB = 0
        indexC = 0
        result = [1]
        valueA = result[indexA] * 2
        valueB = result[indexB] * 3
        valueC = result[indexC] * 5
        while n > len(result):
            value = min(valueA,valueB,valueC)
            result.append(value)
            if valueA == value:
                indexA += 1
                valueA = result[indexA] * 2
            #此处必须都是if,而不能有elif,因为可能存在多种方式同时达到最小值的情况
            if valueB == value:
                indexB += 1
                valueB = result[indexB] * 3
            if valueC == value:
                indexC += 1
                valueC = result[indexC] * 5
        return result[-1]

s = Solution()
print s.nthUglyNumber(8)
                    

                