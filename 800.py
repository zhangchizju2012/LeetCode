#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 23:04:15 2018

@author: zhangchi
"""

class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        self.dic = {}
        self.reverse = {}
        for i in range(10):
            self.dic[str(i)] = i
            self.reverse[i] = str(i)
        for index, item in enumerate(["a","b","c","d","e","f"]):
            self.dic[item] = index + 10
            self.reverse[index + 10] = item
        result = "#"
        for i in range(1,7,2):
            result += self.helper(color[i:i+2])
        return result
    
    def helper(self, s):
        # 两个两个处理就好
        first = self.dic[s[0]]
        second = self.dic[s[1]]
        
        value = float('inf')
        
        if first > 0:
            temp = 16 + (second - (first - 1))
            if temp < value:
                result = self.reverse[first-1] * 2
                value = temp
                
        temp = abs(second - first)
        if temp < value:
            result = self.reverse[first] * 2
            value = temp
            
        if first < 15:
            temp = 16 + ((first + 1) - second)
            if temp < value:
                result = self.reverse[first+1] * 2
                value = temp
                
        return result
    
s = Solution()
print(s.similarRGB("#09f166"))