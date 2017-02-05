#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:03:00 2016

@author: zhangchi
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        diction = {}
        for i in range(len(nums)):
            diction[nums[i]]=i
        nums.sort()
        pointA = 0
        pointB = len(nums)-1
        while nums[pointA] + nums[pointB] != target:
            if pointA == pointB:
                return [-1,-1]
            else:
                if nums[pointA] + nums[pointB] < target:
                    pointA = pointA + 1
                else:
                    pointB = pointB - 1
        return [diction[nums[pointA]], diction[nums[pointB]]]
        '''
        #hash用于建立数值到下标的映射
        hash = {}
        #循环nums数值，并添加映射
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
        #无解的情况
        return [-1, -1]

a = Solution()
print a.twoSum([2,7,11,15],9)