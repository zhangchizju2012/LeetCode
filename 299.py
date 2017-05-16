#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:11:02 2017

@author: zhangchi
"""

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        aValue = 0
        bValue = 0
        secretDic = {}
        guessDic = {}
        for a,b in zip(secret,guess):
            if a == b:
                aValue += 1
            else:
                if a in secretDic:
                    secretDic[a] += 1
                else:
                    secretDic[a] = 1

                if b in guessDic:
                    guessDic[b] += 1
                else:
                    guessDic[b] = 1
        for item in secretDic:
            if item in guessDic:
                bValue += min(secretDic[item],guessDic[item])
        return str(aValue)+'A'+str(bValue)+'B'
        
s = Solution()
print s.getHint("1123","0111")