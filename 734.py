#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 19:51:50 2017

@author: zhangchi
"""

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        
        dic = {}
        for item in pairs:
            if item[0] not in dic:
                dic[item[0]] = set([item[1]])
            else:
                dic[item[0]].add(item[1])
                
            if item[1] not in dic:
                dic[item[1]] = set([item[0]])
            else:
                dic[item[1]].add(item[0])
                
        for a,b in zip(words1, words2):
            if a != b:
                if a not in dic or b not in dic:
                    return False
                if b not in dic[a]:
                    return False
        return True
    
s = Solution()
print s.areSentencesSimilar(["great", "acting","skills"], ["fine","drama", "talent"], [["great", "fine"], ["acting","drama"], ["skills","talent"]])