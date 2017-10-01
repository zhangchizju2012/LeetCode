#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 19:31:19 2017

@author: zhangchi
"""

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lengthA = len(A)
        lengthB = len(B)
        temp = lengthB // lengthA
        # 有可能的话也就这三种长度有可能
        if B in A * temp:
            return temp
        elif B in A * (temp+1):
            return temp + 1
        elif B in A * (temp+2):
            return temp + 2
        else:
            return -1
        
s = Solution()
print s.repeatedStringMatch("abcd","cdabcdab")
# =============================================================================
#         if B in A:
#             return 1
#         else:
#             count = 0
#             index = B.find(A)
#             if index > 0:
#                 if B[:index] in A:
#                     count = 1
#                 else:
#                     return -1
#             elif index == -1:
#                 return -1
# =============================================================================
