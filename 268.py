#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 13:08:53 2017

@author: zhangchi
"""

class Solution(object):
    # 还有位控制的一种方法，来自答案，值得一看
    # https://discuss.leetcode.com/topic/24535/4-line-simple-java-bit-manipulate-solution-with-explaination
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 因为之差一个数，如果全都在的话是0,1,2,3...len(nums)
        return len(nums) * (len(nums) + 1) / 2 - sum(nums)
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 利用hash，很二
        dic = set()
        for item in nums:
            dic.add(item)
        for i in xrange(len(nums)+1):
            if i not in dic:
                return i
