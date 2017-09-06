#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:12:58 2017

@author: zhangchi
"""


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in xrange(1,n):
            if not knows(i, candidate):# 被人认识的才能是candidate
                candidate = i
        for j in xrange(candidate): # 确定前面的人也都认识这个candidate
            if not knows(j, candidate):
                return -1
        for i in xrange(n): # candidate不能认识任何人
            if candidate != i:
                if knows(candidate, i):
                    return -1
        return candidate