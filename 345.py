#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:46:32 2017

@author: zhangchi
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelsIndex = []
        vowelsItem = []
        vowel = "aeiouAEIOU"
        temp = []
        for index,item in enumerate(s):
            if item in vowel:
                vowelsIndex.append(index)
                vowelsItem.append(item)
            temp.append(item)
        vowelsIndex = vowelsIndex[::-1]
        for index,item in enumerate(vowelsIndex):
            temp[item] = vowelsItem[index]
        return "".join(temp)
#==============================================================================
#     # version 1
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         vowelsIndex = {}
#         vowelsItem = []
#         notItem = []
#         vowel = "aeiouAEIOU"
#         for index,item in enumerate(s):
#             if item in vowel:
#                 vowelsIndex[index] = 1
#                 vowelsItem.append(item)
#             else:
#                 notItem.append(item)
#         #notItem = notItem[::-1]
#         index = 0
#         result = ""
#         for i in xrange(len(s)):
#             if i in vowelsIndex:
#                 result += vowelsItem.pop()
#             else:
#                 result += notItem[index]
#                 index += 1
#         return result
#==============================================================================
        
s = Solution()
print s.reverseVowels("hello")
                