#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:24:07 2016

@author: zhangchi

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def __init__(self):
        self.result = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.helper([])
        return self.result
        
    def helper(self,stop):
        if len(stop) == len(self.nums):
            self.result.append(stop)
        else:
            for item in self.nums:
                if item not in stop:
                    self.helper(stop+[item])
                
S = Solution()
print S.permute([1,2,3])        
        
        
        
'''
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        num.sort()
        length = len(num)
        if length == 0:
            return []
        if length == 1:
            return [num]#num 本身就是一个list,所以不用写成[[num]]
        result = []
        a = None
        for i in range(length):
            b = num[i]
            if b == a:
                pass
            else:
                a = b
                temp = self.permute(num[:i]+num[i+1:])
                for item in temp:
                    result.append(item + [num[i]])
        return result
'''
'''
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        length = len(num)
        if length == 0:
            return []
        if length == 1:
            return [num]#num 本身就是一个list,所以不用写成[[num]]
        result = []
        for i in range(length):
            temp = self.permute(num[:i]+num[i+1:])
            for item in temp:
                result.append(item + [num[i]])
        return result
'''
'''
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if len(nums) == 0:
            return []
        result = [[nums[0]]]
        nums = nums[1:]
        while len(nums) > 0:
            temp = nums[0]
            nums = nums[1:]
            temp_result = []
            for item in result:
                for i in range(len(item)+1):
                    temp_result.append(item[:i]+[temp]+item[i:])
            result = temp_result
        return result
'''
'''
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0: 
            return []
        if len(num) == 1: 
            return [num]
        res = []
        for i in range(len(num)):
            for j in self.permute(num[:i] + num[i+1:]):
                res.append([num[i]] + j)
        return res
   '''     