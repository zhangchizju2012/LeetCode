#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 12:01:36 2017

@author: zhangchi
"""

class Solution(object):
    # 自己做的，感觉跟之前回文的一道题比较像 -->5.py
    # 思路：先找到第一个满足条件的，然后之后让条件不断苛刻（长度越来越短）
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        result = None
        for index, item in enumerate(nums):
            temp += item
            if temp >= s:
                result = index + 1
                right = index
                break
        if result is None:
            return 0
        left = 1
        temp = temp - nums[0]
        while right < len(nums) - 1:
            if temp >= s:
                result = right - left + 1
                left += 1
                temp = temp - nums[left-1]
            else:
                right += 1
                left += 1
                temp = temp + nums[right] - nums[left-1]
        while temp >= s:
            result = right - left + 1
            left += 1
            temp = temp - nums[left-1]
        return result
        
s = Solution()
print s.minSubArrayLen(7,[2,3,1,2,4,3])