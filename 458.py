#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:57:52 2017

@author: zhangchi
"""

class Solution(object):
    # 看了答案，不看挺难的：https://discuss.leetcode.com/topic/67666/another-explanation-and-solution
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets == 1:
            return 0
        testNumber = minutesToTest // minutesToDie + 1
        count = 1
        base = testNumber
        while base < buckets:
            count += 1
            base *= testNumber
        return count
        
s = Solution()
print s.poorPigs(26,15,60)