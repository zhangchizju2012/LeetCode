#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:43:30 2017

@author: zhangchi
"""
# bfs, much faster
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        stack = [n]
        tempDict = {}
        result = 0
        while True:
            result += 1
            while len(stack) > 0:
                tempValue = stack.pop()
                temp = int(math.sqrt(tempValue))
                if tempValue == temp ** 2:
                    return result
                else:
                    for i in range(temp,0,-1):
                        if tempValue - i ** 2 not in tempDict:
                            tempDict[tempValue - i ** 2] = 1
            stack = tempDict.keys()
            tempDict = {}

#==============================================================================
# almost the same, the main shortcoming is that tempStack may become large
# bfs, much faster
# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         import math
#         stack = [n]
#         tempStack = []
#         result = 0
#         while True:
#             result += 1
#             while len(stack) > 0:
#                 tempValue = stack.pop()
#                 temp = int(math.sqrt(tempValue))
#                 if tempValue == temp ** 2:
#                     return result
#                 else:
#                     for i in range(temp,0,-1):
#                         tempStack.append(tempValue - i ** 2)
#             stack = tempStack
#             tempStack = []
#==============================================================================

#==============================================================================
# # dfs, too slow
# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         import math
#         temp = int(math.sqrt(n))
#         if n == temp ** 2:
#             return 1
#         else:
#             result = float('inf')
#             for i in range(temp,0,-1):
#                 result = min(result, self.numSquares(n-i**2))
#             return result + 1
#==============================================================================
            
s = Solution()
print s.numSquares(1535)
