#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 21:43:53 2017

@author: zhangchi
"""

class Solution(object):
    # easy after finish 131
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return -1
        result = (length+1) * [float('inf')]
        # add one more item, and assign 0 to it, for the case "aba"
        # 在line 28, 当直接和最后一个回文的时候，可以直接0+1，所有多添加了这么一个数
        result[-2] = 1
        result[-1] = 0
        for i in xrange(length-2,-1,-1):
            temp = float('inf')
            for j in xrange(i,length):
                string = s[i:j+1]
                if string == string[::-1]:
                    temp = min(temp,1+result[j+1])
            result[i] = temp
        return result[0] - 1 
        # in my algorithm, result中的内容意味着切分之后有几块，所求为要切几刀，所以减1
            