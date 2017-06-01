#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:19:17 2017

@author: zhangchi
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s.strip().split(" ")
        temp = temp[::-1]
        result = ""
        for item in temp[:-1]:
            if len(item) > 0:
                result += item + " "
        result += temp[-1]
        return result
        
s = Solution()
#print s.reverseWords("the sky is blue")
print s.reverseWords("   a   b ")