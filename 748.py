#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:35:45 2017

@author: zhangchi
"""

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        result = None
        check = {}
        for item in licensePlate:
            item = item.lower()
            if "a" <= item <= "z":
                if item not in check:
                    check[item] = 1
                else:
                    check[item] += 1
        for item in words:
            if result is None or len(item) < len(result):
                if self.helper(dict(check),item):
                    result = item
        return result
        
    def helper(self, check, item):
        for i in item:
            if i in check:
                check[i] -= 1
        for i in check:
            if check[i] > 0:
                return False
        return True
    
s = Solution()
print s.shortestCompletingWord("1s3 456",["looks", "pest", "stew", "show"])