#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:52:20 2017

@author: zhangchi
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        temp = 0
        result = 0
        for i in range(len(num2)-1,-1,-1):
            prev = 0
            count = temp
            temp += 1
            for j in range(len(num1)-1,-1,-1):
                now = int(num1[j]) * int(num2[i]) + prev
                result += now % 10 * (10 ** count)
                prev = now // 10
                count += 1
            if prev != 0:#Don't miss this part!
                result += prev * (10 ** count)
        return str(result)
        
    def multiply2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        temp = 0
        result = ''
        for i in range(len(num2)-1,-1,-1):
            prev = 0
            count = temp
            temp += 1
            for j in range(len(num1)-1,-1,-1):
                now = int(num1[j]) * int(num2[i]) + prev
                if len(result) - 1 < count:
                    result = str(now % 10) + result
                else:
                    string = str(int(result[len(result)-1-count]) + now % 10)
                    if len(string) == 1:
                        result = result[:len(result)-1-count] + string + result[len(result)-count:]
                    else:
                        result = result[:len(result)-1-count] + string[1] + result[len(result)-count:]
                    # haven't consider string[0] + result[:len(result)-2-count], then the sum can also exceed 10
                    # think about it later.
                                        
                    #result[len(result)-1-count] = str(int(result[len(result)-1-count]) + now % 10)
                    #not allowed, 'str' object does not support item assignment
                prev = now // 10
                count += 1
            if prev != 0:
                result = str(prev) + result
        return result
        
s = Solution()
print s.multiply('457892','370478905')