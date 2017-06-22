#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:05:53 2017

@author: zhangchi
"""

class Solution(object):
    # 不一定重复两次，重复更多次也可以
    # 来自https://discuss.leetcode.com/topic/64979/python-o-n-time-o-1-space
    # http://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
    # 思路：
    # 经过了某一个数，就将该数-1（此处需要将该数加abs，因为之前可能将这个数变成负的了，巧妙之处也在于负数这个记号可以通过abs变回来）
    # 作为index，在index所在的数变成负的，作为记号
    # 之后又经过一次相同的数，发现作为index对应的数是负的，就可以把这个数append到结果取了
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for item in nums:
            if nums[abs(item)-1] > 0:
                nums[abs(item)-1] = -nums[abs(item)-1]
            else:
                result.append(abs(item))
        return result
        
s = Solution()
print s.findDuplicates([4,3,2,7,8,2,3,1])