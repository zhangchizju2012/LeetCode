#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 18:32:35 2018

@author: zhangchi
"""

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for item in A:
            temp = item[::-1]
            tempResult = []
            for i in temp:
                if i == 0:
                    tempResult.append(1)
                else:
                    tempResult.append(0)
            result.append(tempResult)
        return result
        
s = Solution()
i =[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(s.flipAndInvertImage(i))