#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 00:46:37 2017

@author: zhangchi
"""

class Solution(object):
    # 对于follow up的问题，来了一列string,可以有一个dict储存首字母和他们在string list的位置
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lenS = len(s)
        lenT = len(t)
        indexS = 0
        indexT = 0
        while indexS < lenS and indexT < lenT:
            if s[indexS] == t[indexT]:
                indexS += 1
                indexT += 1
            else:
                indexT += 1
        if indexS == lenS:
            return True
        else:
            return False
            
s = Solution()
print s.isSubsequence("axc", "ahbgdc")