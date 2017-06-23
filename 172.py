#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 01:43:27 2017

@author: zhangchi
"""

class Solution(object):
    # 关键是5，10不重要，10也是由5构成的, 把5管好就可以了
    # 自己做的
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        value = 5
        while n // value != 0:
            result += n // value
            value *= 5
        return result
        
s = Solution()
print s.trailingZeroes(11111)