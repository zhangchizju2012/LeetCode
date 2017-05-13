#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:13:24 2017

@author: zhangchi
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        result = {}
        for item in coins:
            result[item] = 1
        for i in xrange(1,amount+1):
            if i not in result:
                minValue = float('inf')
                label = False
                for j in xrange(1,i//2+1):
                    if j in result and (i-j) in result:
                        minValue = min(minValue,result[j]+result[i-j])
                        label = True
                if label == True:
                    result[i] = minValue
        if amount in result:
            return result[amount]
        else:
            return -1
                

#==============================================================================
# class Solution(object):
#     # too slow
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         self.coins = coins
#         self.result = []
#         self.helper(amount,0)
#         if len(self.result) == 0:
#             return -1
#         else:
#             return min(self.result)
#     
#     def helper(self, amount, count):
#         if amount == 0:
#             self.result.append(count)
#         elif amount > 0:
#             for item in self.coins:
#                 self.helper(amount-item,count+1)
#==============================================================================
                
s = Solution()
print s.coinChange([1,2,5],100)