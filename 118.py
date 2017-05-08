#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:52:23 2017

@author: zhangchi
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        else:
            result = [[1]]
            while numRows > 1:
                numRows -= 1
                temp = result[-1]
                wait = [1]
                for i in range(len(temp)-1):
                    wait.append(temp[i]+temp[i+1])
                wait.append(1)
                result.append(wait)
            return result
            
s = Solution()
print s.generate(1)