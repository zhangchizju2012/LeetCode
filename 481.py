#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 00:35:56 2017

@author: zhangchi
"""

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:return 0
        elif n<=3:return 1
        string = '122'
        point = 2
        temp = 2
        count = 1
        length = 3
        while True:
            if temp == 2:
                if string[point] == '2':
                    string += '11'
                    length += 2
                    count += 2
                else:
                    string += '1'
                    length += 1
                    count += 1
                temp = 1
            else:
                if string[point] == '2':
                    string += '22'
                    length += 2
                else:
                    string += '2'
                    length += 1
                temp = 2
            point += 1
            if length == n:
                return count
            elif length > n:
                if temp == 1:
                    return count - 1
                else:
                    return count
    
s = Solution()
print s.magicalString(4567)