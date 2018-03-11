#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:31:21 2018

@author: zhangchi
"""

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        positionList = []
        position = B.find(A[0], 0)
        while position != -1:
            positionList.append(position)
            position = B.find(A[0], position+1)
            
        for item in positionList:
            if (B[item:] + B[:item]) == A:
                return True
        return False

s = Solution()
print(s.rotateString('abcde', 'abced'))