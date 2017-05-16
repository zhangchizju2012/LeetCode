#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:52:10 2017

@author: zhangchi
"""

class Solution(object):
    def checkSame(self,dicCom):
        for item in self.dic:
            if item in dicCom and self.dic[item] == dicCom[item]:
                pass
            else:
                return False
        return True
        
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lengthS = len(s)
        lengthP = len(p)
        if lengthP > lengthS:
            return []
        result = []
        self.dic = {}
        dicCompare = {}
        for i in xrange(lengthP):
            if p[i] in self.dic:
                self.dic[p[i]] += 1
            else:
                self.dic[p[i]] = 1
            
            if s[i] in dicCompare:
                dicCompare[s[i]] += 1
            else:
                dicCompare[s[i]] = 1
        if self.checkSame(dicCompare) == True:
            result.append(0)
        for i in xrange(lengthS-lengthP):
            dicCompare[s[i]] -= 1
            if s[i+lengthP] in dicCompare:
                dicCompare[s[i+lengthP]] += 1
            else:
                dicCompare[s[i+lengthP]] = 1
            if self.checkSame(dicCompare) == True:
                result.append(i+1)
        return result

s = Solution()
print s.findAnagrams("cbaebabacd","abc")