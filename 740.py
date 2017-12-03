#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:34:21 2017

@author: zhangchi
"""

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for item in nums:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        self.information = []
        for item in dic:
            self.information.append([item,dic[item]])
        self.information.sort(key=lambda x:x[0])
        self.length = len(self.information)
        self.dict = {}
        self.helper(0)
        return self.dict[0]
    
    def helper(self, i):
        if i not in self.dict:
            if i == self.length:
                value = 0
            elif i == self.length - 1:
                value = self.information[i][0] * self.information[i][1]
            else:
                value1 = self.information[i][0] * self.information[i][1]
                if self.information[i+1][0] == self.information[i][0] + 1:
                    value1 += self.helper(i+2)
                else:
                    value1 += self.helper(i+1)
                    
                value = max(value1, self.helper(i+1))
            self.dict[i] = value
        return self.dict[i]
    
s = Solution()
print s.deleteAndEarn([])