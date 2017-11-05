#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:35:35 2017

@author: zhangchi
"""

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        dic = {}
        for item in words:
            if len(item) not in dic:
                dic[len(item)] = set([item])
            else:
                dic[len(item)].add(item)
                
        if 1 not in dic:
            return ""
        else:
            left = dic[1]
            now = 2
            while True:
                nextLeft = set()
                if now in dic:
                    for item in dic[now]:
                        if item[:-1] in left:
                            nextLeft.add(item)
                if len(nextLeft) == 0:
                    temp = list(left)
                    temp.sort()
                    return temp[0]
                else:
                    left = nextLeft
                    now += 1
                    
s = Solution()
print s.longestWord( ["a"])