#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:13:24 2017

@author: zhangchi
"""

class Solution(object):
    # 和279很像
    # bfs, improved by using hash table
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        stack = [amount]
        searched = {amount:1}# the only difference
        result = 0
        while len(stack) > 0:
            result += 1
            temp = []
            while len(stack) > 0:
                point = stack.pop()
                for i in coins:
                    value = point - i
                    if value == 0:
                        return result
                    elif value > 0 and value not in searched:
                        temp.append(value)
                        searched[value] = 1 # the only difference
            stack = temp
        return -1

s = Solution()
print s.coinChange([431,62,88,428],9084)

#==============================================================================
# class Solution(object):
#     # bfs
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         if amount == 0:
#             return 0
#         stack = [amount]
#         searched = [amount]
#         result = 0
#         while len(stack) > 0:
#             result += 1
#             temp = []
#             while len(stack) > 0:
#                 point = stack.pop()
#                 for i in coins:
#                     value = point - i
#                     if value == 0:
#                         return result
#                     elif value > 0 and value not in searched:
#                         temp.append(value)
#                         searched.append(value)
#             stack = temp
#         return -1
#==============================================================================
                    
s = Solution()
print s.coinChange([3,7,405,436],8839)
#print s.coinChange([2],3)

#==============================================================================
# class Solution(object):
#     # dp
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         if amount == 0:
#             return 0
#         result = {}
#         for item in coins:
#             result[item] = 1
#         for i in xrange(1,amount+1):
#             if i not in result:
#                 minValue = float('inf')
#                 label = False
#                 for j in xrange(1,i//2+1):
#                     if j in result and (i-j) in result:
#                         minValue = min(minValue,result[j]+result[i-j])
#                         label = True
#                 if label == True:
#                     result[i] = minValue
#         if amount in result:
#             return result[amount]
#         else:
#             return -1
#==============================================================================
                

#==============================================================================
# class Solution(object):
#     # too slow, dfs
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
                