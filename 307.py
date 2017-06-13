#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:22:05 2017

@author: zhangchi
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.i = 0
        self.j = len(nums)-1
        self.temp = sum(nums[self.i:self.j+1])
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if self.i <= i <= self.j:
            self.temp = self.temp - self.nums[i] + val
        self.nums[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < self.i:
            self.temp += sum(self.nums[i:self.i])
        else:
            self.temp -= sum(self.nums[self.i:i])
        self.i = i
        if j > self.j:
            self.temp += sum(self.nums[self.j+1:j+1])
        else:
            self.temp -= sum(self.nums[j+1:self.j+1])
        self.j = j
        return self.temp
            
#==============================================================================
# class NumArray(object):
#     #这个也能通过，但是慢不少
# 
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
# 
#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: void
#         """
#         self.nums[i] = val
#         
# 
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         return sum(self.nums[i:j+1])
#==============================================================================
