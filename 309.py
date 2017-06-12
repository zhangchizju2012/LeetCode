#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:53:53 2017
Edited on Mon Jun  12 17:47:05 2017

@author: zhangchi
"""

class Solution(object):
    # inspired by https://discuss.leetcode.com/topic/30680/share-my-dp-solution-by-state-machine-thinking
    # 加一句话： 
    # s0[i]意思是:the max profit you can get if you are at stage s0 after day i
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        s0 = [0]
        s1 = [-prices[0]]
        s2 = [-float('inf')] #为了配合s0.append(max(s0[i-1],s2[i-1]))
        for i in xrange(1,len(prices)):
            s0.append(max(s0[i-1],s2[i-1]))
            s1.append(max(s1[i-1],s0[i-1]-prices[i]))
            s2.append(s1[i-1]+prices[i])
        return max(s0[-1],s2[-1])
#==============================================================================
#     # wrong
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) == 0:
#             return 0
#         result = 0
#         last = prices[0]
#         previous = 0
#         i = 0
#         while i < len(prices):
#             item = prices[i]
#             i += 1
#             if item >= last:
#                 #if previous is not None:
#                 result += previous
#                 previous = item - last
#                 last = item
#             else:
#                 if i < len(prices):
#                     if prices[i] - last + previous > max(prices[i] - item, previous):#[1, 2, 3, 5, 4, 7]
#                         previous = prices[i] - last + previous
#                         last = prices[i]
#                         i += 1
#                     elif prices[i] - item <= previous:
#                         result += previous
#                         last = prices[i]
#                         previous = 0#feels like restart
#                         i += 1
#                     else:
#                         last = prices[i]
#                         previous = prices[i] - item
#                         i += 1
#                 else:
#                     result += previous
#                     previous = 0
#         result += previous
#         return result
#==============================================================================
    
s = Solution()
# works for [2,3,5,8,3,8], didn't consider [2,6]
# result for [2,3,5,8,3,8] should be 8, it's right
print s.maxProfit([1, 2, 3, 0, 2])