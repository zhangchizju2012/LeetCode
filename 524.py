#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:22:37 2017

@author: zhangchi
"""

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        result = ""
        for item in d:
            if len(item) > len(s):
                pass
            else:
                difference = len(s) - len(item)
                i = 0
                j = 0
                label = True
                itemLength = len(item)
                while label:
                    if item[i] == s[j]:
                        i += 1
                        j += 1
                    else:
                        j += 1
                        difference -= 1
                    if difference < 0:
                        label = False
                    if i == itemLength:
                        break
                if label == True:
                    if len(item) > len(result):
                        result = item
                    elif len(item) == len(result):
                        if item < result:
                            result = item
        return result
                    