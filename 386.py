#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:28:30 2017

@author: zhangchi
"""

class Solution(object):
    # 效率还不够高
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 9:
            return [i for i in xrange(1,n+1)]
        self.n = n
        self.result = []
        for i in xrange(1,10):
            self.helper(i)
        return self.result
        
    
    def helper(self, now):
        if now <= self.n:
            self.result.append(now)
            for i in xrange(10):
                if self.helper(now*10+i) == False:
                    break
            return True
        else:
            return False
#==============================================================================
#     def lexicalOrder(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         if n <= 9:
#             return [i for i in xrange(1,n+1)]
#         self.n = n
#         self.result = []
#         for i in xrange(1,10):
#             self.helper(i)
#         return self.result
#         
#     
#     def helper(self, now):
#         if now <= self.n:
#             self.result.append(now)
#             for i in xrange(10):
#                 self.helper(now*10+i)
#==============================================================================
        
s = Solution()
print s.lexicalOrder(1)