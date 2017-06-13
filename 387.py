#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:54:43 2017

@author: zhangchi
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for item in s:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        for index,item in enumerate(s):
            if dic[item] == 1:
                return index
        return -1