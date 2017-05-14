#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 10:04:28 2017

@author: zhangchi
"""

class Solution(object):
    def __init__(self):
        self.result = {}
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        length1 = len(word1)
        length2 = len(word2)
        self.word1 = word1
        self.word2 = word2
        for i in xrange(length1+1):
            self.result[(i,0)] = i
        for i in xrange(length2+1):
            self.result[(0,i)] = i
        return self.helper(length1,length2)
    def helper(self,i,j):
        if (i,j) not in self.result:
            if self.word1[i-1] == self.word2[j-1]:
                temp = self.helper(i-1,j-1)
            else:
                temp = min(self.helper(i-1,j),self.helper(i,j-1)) + 1
                #分别代表替换，删除，插入（向string1插入就相当于删除string2）
            self.result[(i,j)] = temp
        return self.result[(i,j)]
        
s = Solution()
print s.minDistance("a", "b")