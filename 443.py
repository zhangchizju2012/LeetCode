#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:37:42 2017

@author: zhangchi
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        charList = []
        countList = []
        previous = chars[0]
        count = 1
        for i in xrange(1,len(chars)):
            if chars[i] == previous:
                count += 1
            else:
                charList.append(previous)
                countList.append(count)
                previous = chars[i]
                count = 1
        charList.append(previous)
        countList.append(count)
        
        index = 0
        for a, b in zip(charList,countList):
            chars[index] = a
            index += 1
            
            if b > 1:
                temp = str(b)
                for i in xrange(len(temp)):
                    chars[index] = temp[i]
                    index += 1
        return index
    
s = Solution()
print s.compress(["a"])