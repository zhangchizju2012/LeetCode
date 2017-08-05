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
        length = len(nums)
        index = self.partition(0,length-1)
        left = 0
        right = length - 1
        while True:
            if index == k - 1:
                return self.nums[index]
            elif index < k - 1:
                left = index+1
            else:
                right = index-1
            index = self.partition(left,right)
        
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
                self.nums[left], self.nums[right] = self.nums[right], self.nums[left]
                left += 1
                right -= 1
            else:
                left -= 1
                self.nums[left], self.nums[first] = self.nums[first], self.nums[left]
                break
        return left
        
s = Solution()
for i in xrange(1,9):
    print s.findKthLargest([6,5,5,4,4,4,3,2,1],i)
        


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
