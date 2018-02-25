#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:58:26 2018

@author: zhangchi
"""

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic = {}
        reverse = {}
        for index, item in enumerate(S):
            dic[item] = index
            reverse[index] = item
            
        temp = []
        val = 100
        for item in T:
            if item in dic:
                temp.append(dic[item])
            else:
                temp.append(val)
                dic[item] = val
                reverse[val] = item
                val += 1
        temp.sort()
        result = ""
        for item in temp:
            result += reverse[item]
        return result
    
s = Solution()
print s.customSortString("cba","abcded")