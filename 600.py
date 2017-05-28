#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 20:04:45 2017

@author: zhangchi
"""

class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        dic = {0:1,1:2,2:3}
        for i in range(3,32):
            dic[i] = dic[i-2] + dic[i-1]
        temp = [0] * 32
        for i in range(32):
            if num & (2**i) > 0:
                temp[i] = 1
        temp = temp[::-1]
        result = 0
        for index, item in enumerate(temp):
            if item == 1:
                if index == 0 or temp[index-1] == 0:
                    result += dic[31-index]
                else:
                    result += dic[31-index]
                    return result
        result += 1
        return result
        
s = Solution()
print s.findIntegers(4)