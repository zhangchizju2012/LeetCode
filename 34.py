#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 15:58:29 2017

@author: zhangchi
"""

class Solution(object):
    # 思路就是两边的范围都用binary search
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        self.nums = nums
        self.target = target
        self.left = -1
        self.right = -1
        self.length = len(nums)
        self.helperLeft()
        if self.left == -1:
            return [-1,-1]
        self.helperRight()
        return [self.left,self.right]
        
    def helperRight(self):
        left = 0
        right = self.length - 1
        if self.nums[right] == self.target:
            self.right = right
        elif self.nums[right] < self.target or self.nums[0] > self.target:
            pass
        else:
            if self.nums[left] == self.target:
                self.right = left
            label = True
            while right-left >= 1 and label:
                if right - left == 1:
                    label = False
                middle = (left + right) // 2
                if self.nums[middle] == self.target:
                    self.right = middle
                if self.nums[middle] <= self.target:
                    left = middle
                else:
                    right = middle
        
    def helperLeft(self):
        left = 0
        right = self.length - 1
        if self.nums[left] == self.target:
            self.left = 0
        elif self.nums[right] < self.target or self.nums[0] > self.target:
            pass
        else:
            if self.nums[right] == self.target:
                self.left = right
            label = True
            while right-left >= 1 and label:
                if right - left == 1:
                    label = False
                middle = (left + right) // 2
                if self.nums[middle] == self.target:
                    self.left = middle
                if self.nums[middle] >= self.target:
                    right = middle
                else:
                    left = middle

s = Solution()
print s.searchRange([5],5 )