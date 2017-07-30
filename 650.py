#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 19:59:27 2017

@author: zhangchi
"""

class Solution(object):
    # 自己写的，比赛题
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        import math
        temp = []
        for i in xrange(2,int(math.sqrt(n))+1):
            if n%i == 0:
                temp.append((i,n/i))
        if len(temp) == 0: #质数的话n是多少答案就多少，根本不能翻倍
            return n
        else:
            result = float('inf')
            for a,b in temp:
                result = min(result, self.minSteps(a)+b)#先得到a,再不断翻倍
            for b,a in temp:
                result = min(result, self.minSteps(a)+b)
            return result
            
s = Solution()
print s.minSteps(18)