#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Review on Thu Aug  3 22:59:21 2017

@author: zhangchi
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.nums = nums
        
    def partition(self, first, last):
        pivot = self.nums[first]
        left = first + 1
        right = last
        while True:
            while left <= right and self.nums[left] >= pivot:
                left += 1
            while right >= left and self.nums[right] <= pivot:
                right -= 1
            if left < right:
                
            
        


"""
Created on Thu Apr 13 22:38:11 2017

@author: zhangchi
"""

#==============================================================================
# import heapq
# 
# class Solution(object):
#     # complexity comparison can be found here:
#     # https://leetcode.com/problems/kth-largest-element-in-an-array/#/solutions
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         heap = []
#         for item in nums:
#             heapq.heappush(heap,-item)
#         count = 1
#         while count <= k:
#             result = -heapq.heappop(heap)
#             count += 1
#         return result
#         
#     def findKthLargest2(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         nums.sort(reverse=True)
#         return nums[k-1]
#==============================================================================
