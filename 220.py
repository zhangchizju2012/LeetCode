#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 12:37:13 2017

@author: zhangchi
"""

class Solution(object):
    # 看答案写的：https://discuss.leetcode.com/topic/27608/java-python-one-pass-solution-o-n-time-o-n-space-using-buckets
    # 思路：把一个范围的数对应到一个数，这样就可以跟219差不多了(通过change = item /  length)
    # 不太一样的是，符合要求的也可能在change-1或者change+1处
    # 以及为了能和change-1和change+1处的数比较，dict里的value保存的是实际的数(key是变化后的数)
    # 为了满足下标的要求，当某index已经超过满足需求的时候，需要及时把他从dict中去掉（line36）
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False
        dic = {}
        length = t + 1
        for index, item in enumerate(nums):
            change = item /  length
            if change in dic:
                return True
            if (change - 1) in dic and abs(dic[change-1]-item) <= t:
                return True
            if (change + 1) in dic and abs(dic[change+1]-item) <= t:
                return True
            dic[change] = item
            if index >= k:
                dic.pop(nums[index-k]/length)
        return False
#==============================================================================
#     # 复杂度为 len(nums) * t
#     # 思路：建一个dict，key是值，value是出现该值index最大可以是多少
#     def containsNearbyAlmostDuplicate(self, nums, k, t):
#         """
#         :type nums: List[int]
#         :type k: int
#         :type t: int
#         :rtype: bool
#         """
#         dic = {}
#         for index, item in enumerate(nums):
#             if item not in dic or dic[item] < index:#就算出现了这个值，如果超范围了，也没用
#                 for i in xrange(-t,t+1):
#                     dic[item+i] = index + k
#             else:
#                 return True
#         return False
#==============================================================================
