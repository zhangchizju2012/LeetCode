#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:32:58 2017

@author: zhangchi
"""
class Solution(object):
    # O(n) 复杂度，成对出现，第一次是2，第二次是4，再是8，每次结果加1
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        result = [0,1]
        count = 1
        nextResult = []
        while True:
            for item in result:
                nextResult.append(item+1)
                count += 1
                if count == num:
                    return result + nextResult
            result += nextResult
            nextResult = []

# 下面的也可以，复杂度较高
#==============================================================================
# class Solution(object):
#     def countBits(self, num):
#         """
#         :type num: int
#         :rtype: List[int]
#         """
#         result = []
#         for i in xrange(num+1):
#             result.append(self.helper(i))
#         return result
#         
#     def helper(self, n):
#         count = 0
#         temp = 1
#         while temp <= n:
#             if temp & n > 0:
#                 count += 1
#             temp *= 2
#         return count
#==============================================================================
        
s = Solution()
print s.countBits(4)