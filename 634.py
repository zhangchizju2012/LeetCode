#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:39:30 2017

@author: zhangchi
"""
class Solution(object):
    # 看了Fei Wang的代码
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 1
        der_0 = 0
        der_1 = 1
        idx = 3
        # dp[n] = (n-1) * (dp[n-1]+dp[n-2])
        # 第一个数可以放到后面（n-1）个坑的任意一个位置，假设该位置是m，如果原来在位置m的数放到了第一个数的位置，
        # 则剩下的问题是dp[n-2]，若没有，则是dp[n-1]
        while idx < n+1:
            der_new = (idx-1) * (der_0 + der_1) % 1000000007 # 这一步是关键
            der_0 = der_1
            der_1 = der_new
            idx += 1
        return (der_1 % 1000000007)
# #自己的解法错的，考虑到了第一个数可以放到后面（n-1）个坑的任意一个位置，假设该位置是m，原来在位置m的数可以放到了第一个数的位置，
# #也可以不放到那个位置，考虑到了这个问题，但是没有解决。还在想可能是三个数之间交换位置，剩下的不交换，四个数之间交换位置，
# #剩下的不交换，于是有了下面的代码。但这样还是错的，比方说6，如果拆分成2和4，这个4可能又是2和2组成的，这样的话又存在重复

#==============================================================================
# #错的，考虑到了第一个数可以放到后面（n-1）个坑的任意一个位置，假设该位置是m，原来在位置m的数可以放到了第一个数的位置，
# #也可以不放到那个位置，考虑到了这个问题，但是没有解决。还在想可能是三个数之间交换位置，剩下的不交换，四个数之间交换位置，
# #剩下的不交换，于是有了下面的代码。但这样还是错的，比方说6，如果拆分成2和4，这个4可能又是2和2组成的，这样的话又存在重复
# class Solution(object):
#     def findDerangement(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         self.temp = 10**9 + 7
#         self.dic = {1:0,2:1}
#         return self.helper(n)
#             
#     def helper(self, n):
#         if n not in self.dic:
#             length = n // 2
#             fenzi = 1
#             fenmu = n
#             result = 0
#             if n % 2 == 0:
#                 for i in xrange(2,length):
#                     fenzi *= i
#                     fenmu *= (n-i+1)
#                     result += (fenmu/fenzi) * self.helper(i) *self.helper(n-i)
#                 fenzi *= length
#                 fenmu *= (n-length+1)
#                 result += (fenmu/fenzi) * self.helper(length) *self.helper(length) / 2
#             else:
#                 for i in xrange(2,length+1):
#                     fenzi *= i
#                     fenmu *= (n-i+1)
#                     result += (fenmu/fenzi) * self.helper(i) *self.helper(n-i)
#             result += self.helper2(n)
#             self.dic[n] = result % self.temp
#         return self.dic[n]
# 
#     def helper2(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         temp = 10**9 + 7
#         if n == 1:
#             return 0
#         else:
#             result = 1
#             for i in xrange(1,n):
#                 result *= i
#                 result = result % (temp)
#             return result
#==============================================================================
s = Solution()
print s.findDerangement(6)