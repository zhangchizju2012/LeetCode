#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 00:17:57 2017

@author: zhangchi
"""

class Solution:
    def __init__(self):
        self.result = {}

    def combine(self,n,k):
        if (n,k) in self.result:
            return self.result[(n,k)]
        else:
            if k == 1:
                temp = []
                for i in range(n):
                    temp.append([i+1])
                self.result[(n,k)] = temp
                return temp
            elif k == n:
                temp = []
                for i in range(n):
                    temp.append(i+1)
                self.result[(n,k)] = [temp]
                return [temp]
            else:
                partOne = self.combine(n-1,k)
                partTwo = self.combine(n-1,k-1)
                for item in partTwo:
                    partOne.append(item+[n])
                self.result[(n,k)] = partOne
                return partOne
                
s = Solution()
print s.combine(30,13)
#print len(s.combine(10,7))
                