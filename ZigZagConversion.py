#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:14:05 2016

@author: zhangchi
"""

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    slength = len(s)
    output = ''
    grouplength = 2 * numRows - 2
    if grouplength == 0:
        return s
    for i in range(numRows):
        index = i
        while index < slength:
            output = output + s[index]
            number = index % grouplength
            if number <= numRows - 1:
                gap = grouplength - 2 * number
                if gap == 0:
                    gap = grouplength
                index = index + gap
            if number > numRows - 1:
                gap = 2 * grouplength - 2 * number
                index = index + gap
    return output
    
print convert("123456789012345678901234567890", 6)
        