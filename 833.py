#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 18:37:23 2018

@author: zhangchi
"""

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        if len(indexes) == 0:
            return S
        result = ""
        temp = []
        for a,b,c in zip(indexes, sources, targets):
            temp.append([a,b,c])
        temp.sort(key=lambda x:x[0])
        for item in temp:
            item.append(item[0]+len(item[1]))
        temp.append([len(S),0,0,0])
            
        result += S[:temp[0][0]]
        for index, item in enumerate(temp[:-1]):
            if S[item[0]:item[-1]] == item[1]:
                result += item[2]
            else:
                result += S[item[0]:item[-1]]
            result += S[item[-1]:temp[index+1][0]]
        return result
        
s = Solution()
S = "abcd"
indexes = [0]
sources = ["a"]
targets = ["eee"]
print(s.findReplaceString(S, indexes, sources, targets))