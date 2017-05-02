#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:54:24 2017

@author: zhangchi
"""

class Solution(object):
    # inspired by https://segmentfault.com/a/1190000003709122
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        result = [True] * n
        result[0] = result[1] = False
        count = 0
        for i in xrange(2,n):
            # xrange is better than range
            # using range will result in Memory Limit Exceeded
            # in the future, we should use xrange
            if result[i] == True:
                count += 1
                for j in xrange(2*i,n,i):
                    result[j] = False
        return count
        
s = Solution()
print s.countPrimes(1500000)