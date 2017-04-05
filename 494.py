#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 00:47:23 2017

@author: zhangchi
"""

class Solution0(object):
    def __init__(self):
        self.count = 0
        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.helper(nums,S)
        return self.count
    
    def helper(self, nums, S):
        if len(nums) == 0:
            if S == 0:
                self.count += 1
        else:
            self.helper(nums[1:],S-nums[0])
            self.helper(nums[1:],S+nums[0])
            
class Solution1(object):
    def __init__(self):
        self.count = 0
        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.helper(nums,S,0)
        return self.count
          
    def helper(self, nums, S, start):
        if len(nums[start:]) == 0:
            if S == 0:
                self.count += 1
        else:
            self.helper(nums,S-nums[start],start+1)
            self.helper(nums,S+nums[start],start+1)
        
class Solution2(object):      
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.helper(nums,S,0)
          
    def helper(self, nums, S, start):
        if len(nums[start:]) == 0:
            return S == 0
        else:
            ct1 = self.helper(nums,S-nums[start],start+1)
            ct2 = self.helper(nums,S+nums[start],start+1)
            return ct1 + ct2
            
class Solution(object):
    def __init__(self):
        self.dictionary = {}
        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.helper(nums,S,0)
          
    def helper(self, nums, S, start):
        if len(nums[start:]) == 0:
            if S == 0:
                return 1
            else:
                return 0
        else:
            if (start+1, S-nums[start]) in self.dictionary:
                ct1 = self.dictionary[(start+1, S-nums[start])]
            else:
                ct1 = self.helper(nums,S-nums[start],start+1)
                self.dictionary[(start+1, S-nums[start])] = ct1
            if (start+1, S+nums[start]) in self.dictionary:
                ct2 = self.dictionary[(start+1, S+nums[start])]
            else:
                ct2 = self.helper(nums,S+nums[start],start+1)
                self.dictionary[(start+1, S+nums[start])] = ct2
            return ct1 + ct2
s = Solution()
print s.findTargetSumWays([1,2,3,4,5,6,7,8,9,10,11,12],4)
#print s.findTargetSumWays([29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38],35)