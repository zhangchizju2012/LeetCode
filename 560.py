#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 09:28:30 2017

@author: zhangchi
"""
class Solution(object):
    # by myself, didn't look any materials
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 先把整个数组扫描一遍，建立字典
        dic = {}
        temp = 0
        for item in nums:
            temp += item
            if temp in dic:
                dic[temp] += 1
            else:
                dic[temp] = 1
        result = 0
        temp = 0
        for item in nums:
            # 对去掉前n个数后的部分进行考虑（前n个数的和为temp）
            # 去掉之后接下来的（前1个数，前2个数）前m个数的和如果刚好达到k,则满足题意
            # 这样的数的个数为dic[k+temp]
            if k + temp in dic:
                result += dic[k+temp]
            # temp还没加东西的时候，相当于从0开始的，所有可能性（0到1，0到2，0到3...0到最后）
            # temp加了一个东西的时候，相当于从1开始的，所有可能性（1到2，1到3，1到4...1到最后），以此类推
            temp += item # 和 k + temp in dic结合起来，相当于把前n个数给去掉
            dic[temp] -= 1 # 避免干扰后面
        return result
#==============================================================================
# slow, brute force
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         result = 0
#         length = len(nums)
#         for i in range(length):
#             temp = 0
#             for j in range(i,length):
#                 temp += nums[j]
#                 if temp == k:
#                     result += 1
#         return result
#==============================================================================
nums = [1,2,3,-5,6]
s = Solution()
print s.subarraySum(nums,1)