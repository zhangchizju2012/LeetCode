#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:26:55 2017

@author: zhangchi
"""
import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        count = 0
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                count += i
                if num / i != i:
                    count += num / i
        count += 1
        return count == num
            
s = Solution()
print s.checkPerfectNumber(6)