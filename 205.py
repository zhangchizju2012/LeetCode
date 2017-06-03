#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 17:13:23 2017

@author: zhangchi
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sDic = {}
        for index, item in enumerate(s):
            if item in sDic:
                sDic[item].append(index)
            else:
                sDic[item] = [index]
        tDic = {}
        for index, item in enumerate(t):
            if item in tDic:
                tDic[item].append(index)
            else:
                tDic[item] = [index]
        if len(sDic) != len(tDic):
            return False
        searched = {}
        for a,b in zip(s,t):
            if a not in searched:
                if sDic[a] != tDic[b]:
                    return False
                else:
                    searched[a] = 1
        return True
        
s = Solution()
print s.isIsomorphic("paper", "title")