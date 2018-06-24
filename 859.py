#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 18:31:05 2018

@author: zhangchi
"""

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        else:
            dic = {}
            tempA = None
            tempB = None
            for a,b in zip(A,B):
                if a == b:
                    if a in dic:
                        dic[a] += 1
                    else:
                        dic[a] = 1
                else:
                    if tempA is None:
                        tempA = a
                        tempB = b
                    else:
                        if b == tempA and a == tempB:
                            pass
                        else:
                            return False
            if tempA is not None:
                return True
            else:
                for item in dic:
                    if dic[item] > 1:
                        return True
                return False
            
s = Solution()
print s.buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb")