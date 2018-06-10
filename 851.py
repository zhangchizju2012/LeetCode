#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 19:05:34 2018

@author: zhangchi
"""
# 找肯定比自己富（包括自己）中，比自己（包括自己）安静的
# recursion解
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        self.quiet = quiet
        self.dic = {}
        for i in range(len(quiet)):
            self.dic[i] = []
        for item in richer:
            self.dic[item[1]].append(item[0])
            
        result = [0] * len(quiet)
        self.temp = {}
        
        for i in range(len(quiet)):
            if len(self.dic[i]) == 0:
                self.temp[i] = (i, quiet[i])
                result[i] = i
        for i in range(len(quiet)):
            if len(self.dic[i]) > 0:
                index, value = self.helper(i)
                result[i] = index
        return result
                        
    def helper(self, i):
        if i in self.temp:
            return self.temp[i]
        else:
            index = i
            value = self.quiet[i]
            for item in self.dic[i]:
                if item in self.temp:
                    index_temp, value_temp = self.temp[item]
                else:
                    index_temp, value_temp = self.helper(item)
                if value_temp < value:
                    index = index_temp
                    value = value_temp
            self.temp[i] = (index, value)
            return self.temp[i]
        
s = Solution()
print s.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0])