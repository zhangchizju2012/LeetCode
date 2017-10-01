#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:10:58 2017

@author: zhangchi
"""

class Solution(object):
    # 典型的DP
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        self.n = N
        self.dic = {}
        return float(self.helper(r, c, K)) / float(8 ** K)
        
    def helper(self, r, c, k):
        if (0 <= r < self.n and 0 <= c < self.n) is False:
            return 0
        elif k == 0:
            return 1
        elif (r, c, k) not in self.dic:
            count = self.helper(r-2,c-1,k-1) + self.helper(r-1,c-2,k-1) + self.helper(r-2,c+1,k-1) + self.helper(r-1,c+2,k-1) +\
                    self.helper(r+2,c-1,k-1) + self.helper(r+1,c-2,k-1) + self.helper(r+2,c+1,k-1) + self.helper(r+1,c+2,k-1)
            self.dic[(r, c, k)] = count
        return self.dic[(r, c, k)]
    
s = Solution()
print s.knightProbability(3, 2, 0, 0)