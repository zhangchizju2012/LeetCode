#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:48:29 2017

@author: zhangchi
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= 2:
            hold = [-float('inf')] * 2
            # 重要的是保证release的第一个是0，且不会被更新，这是表示第一个买的动作之前，账户里是0块钱，其他说明同123.py
            release = [0] * 3 #[0] + [-float('inf')] * k
            for item in prices:
                for i in xrange(len(hold)):
                    label = False
                    if release[i]-item > hold[i]:
                        hold[i] = release[i]-item
                        label = True
                    if hold[i]+item > release[i+1]:
                        release[i+1] = hold[i]+item
                        label = True
                    if label == False:
                        break
                if hold[-2] != hold[-1] or release[-2] != release[-1]:
                    hold.append(-float('inf'))
                    release.append(0)
            return hold, release
    
# =============================================================================
#     def maxProfit(self, k, prices):
#         """
#         :type k: int
#         :type prices: List[int]
#         :rtype: int
#         """
#         if k >= 2:
#             hold = [-float('inf')] * 2
#             # 重要的是保证release的第一个是0，且不会被更新，这是表示第一个买的动作之前，账户里是0块钱，其他说明同123.py
#             release = [0] * 3 #[0] + [-float('inf')] * k
#             for index,item in enumerate(prices):
#                 for i in xrange(len(hold)):
#                     hold[i] = max(hold[i],release[i]-item)
#                     release[i+1] = max(release[i+1],hold[i]+item)
#                 if index != (len(prices)-1) and (hold[-2] != hold[-1] or release[-2] != release[-1]):
#                     hold.append(-float('inf'))
#                     release.append(0)
#             return hold, release
# =============================================================================
    
s = Solution()
#b = 1000000000
c,d= s.maxProfit(b,a)
    
# =============================================================================
#     def maxProfit(self, k, prices):
#         """
#         :type k: int
#         :type prices: List[int]
#         :rtype: int
#         """
#         length = len(prices)
#         k = min(k, length)
#         hold = [-float('inf')] * k
#         # 重要的是保证release的第一个是0，且不会被更新，这是表示第一个买的动作之前，账户里是0块钱，其他说明同123.py
#         release = [0] * (k + 1) #[0] + [-float('inf')] * k
#         for item in prices:
#             for i in xrange(k):
#                 hold[i] = max(hold[i],release[i]-item)
#                 release[i+1] = max(release[i+1],hold[i]+item)
#         return release[-1]
# =============================================================================