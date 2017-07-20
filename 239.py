#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:07:37 2017

@author: zhangchi
"""

class Solution(object):
    # 现在的是自己写的
    # should can be optimized
    # https://discuss.leetcode.com/topic/26480/o-n-solution-in-java-with-two-simple-pass-in-the-array
    # 这个解法还没搞懂为啥
    # 看起来还有用deque的解法
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [max(nums[:k])]
        for i in xrange(k,len(nums)):
            if nums[i-k] == result[-1]: # 跟拿掉的那个数相同，才对整个进行扫描
                result.append(max(nums[i+1-k:i+1]))
            else:
                result.append(max(nums[i],result[-1]))
        return result
        
s = Solution()
print s.maxSlidingWindow([1],1)
        