#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 19:48:47 2017

@author: zhangchi
"""

class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        self.dic = {}
        for i in xrange(n+1):
            self.dic[(i,0)] = 1
#==============================================================================
##不用加，当然加了也不会影响
#         for i in xrange(2,n+1):
#             self.dic[(i,1)] = i - 1
#==============================================================================
        return self.helper(n,k)
        
    def helper(self, n, k):
#==============================================================================
##不用加，当然加了也不会影响
#         if n * (n-1) / 2 < k:
#             return 0
#         elif n * (n-1) / 2 == k:
#             return 1
#==============================================================================
        if (n,k) in self.dic:
            return self.dic[(n,k)]
        else:
            count = 0
            for i in xrange(min(k+1,n)):
                count += self.helper(n-1,k-i)
                count = count % (10**9+7)
            self.dic[(n,k)] = count
            return self.dic[(n,k)]
                            
s = Solution()
print s.kInversePairs(223,145)