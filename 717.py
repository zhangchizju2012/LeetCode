#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:30:16 2017

@author: zhangchi
"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits = bits[::-1]
        while len(bits) > 0:
            if len(bits) == 1:
                return True
            else:
                temp = bits.pop()
                if temp == 1:
                    bits.pop()
        return False
    
s = Solution()
print s.isOneBitCharacter([0])