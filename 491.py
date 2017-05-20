#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 06:19:21 2017

@author: zhangchi
"""

#利用dfs和for循环产生子序列（还是bfs？搞不太清楚了）
class Solution(object):
    # more efficient
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return []
        result = [[]]
        for value in nums:
            temp = []
            for item in result:
                temp.append(item)
                if len(item) == 0 or value >= item[-1]:
                    temp.append(item+[value])
            result = temp
        dic = {}
        # 通过hashmap来避免重复
        for item in result:
            dic[tuple(item)] = 1
        final = []
        for item in dic:
            if len(item) >= 2:
                final.append(list(item))
        return final

#==============================================================================
# class Solution(object):
#     def findSubsequences(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) <= 1:
#             return []
#         # not sort, nums.sort()
#         self.nums = nums
#         length = len(nums)
#         self.length = length
#         result = {}
#         for i in xrange(2 ** length):
#             tempList = self.helper(i)
#             if len(tempList) >= 2:
#                 if tempList not in result:
#                     result[tempList] = 1
#         final = []
#         for item in result:
#             final.append(list(item))
#         return final
#             
#     def helper(self,value):
#         temp = []
#         for i in xrange(self.length):
#             if value & (2**i) > 0:
#                 if len(temp) == 0 or self.nums[i] >= temp[-1]:
#                     temp.append(self.nums[i])
#         return tuple(temp)
#==============================================================================
        
s = Solution()
#print s.findSubsequences([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print s.findSubsequences([10,-14,-45,-72,-86,38,-10,15,-48,82,84,88,-22,-89,53])