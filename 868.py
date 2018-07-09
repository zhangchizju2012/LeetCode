#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 18:04:13 2018

@author: zhangchi
"""

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A[0])
        result = [[] for _ in range(row)]
        for line in A:
            for index, item in enumerate(line):
                result[index].append(item)
        return result

s = Solution()
print s.transpose([[1,2,3],[4,5,6]])