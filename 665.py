#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:43:57 2017

@author: zhangchi
"""

class Solution(object):
    # 其实就是一个突然大，然后接下来一个突然变小
    # 有两种策略，忽略大的和忽略小的
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        label = True
        last = nums[0]
        count = 0
        for i in xrange(1,len(nums)):
            if nums[i] >= last:
                last = nums[i]
            else:#忽略小的
                count += 1
                if count > 1:
                    label = False
                    break
                
        if label is True:
            return True
        else:   
            # 忽略大的
            last = nums[0]
            before = -float('inf')
            count = 0
            for i in xrange(1,len(nums)):
                if nums[i] >= last:
                    before = last
                    last = nums[i]
                else:
                    count += 1
                    if count > 1:
                        return False
                    else:
                        if nums[i] >= before:
                            last = nums[i]
            return True
    
s = Solution()
print s.checkPossibility([4,2,1])

#[2,3,3,2,4]
#[4,2,3]