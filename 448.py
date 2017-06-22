#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 20:48:51 2017

@author: zhangchi
"""

class Solution(object):
    # 这是做完442，268后自己想的，受那些启发
    # 回顾442， 268答案解法
    # 思路：出现过的item都在他对应的abs(item)-1处做记号（变成负的）
    # 最后还是为正的index对应的item就是缺失的item
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for item in nums:
            if nums[abs(item)-1] > 0:
                nums[abs(item)-1] = -nums[abs(item)-1]
        result = []
        for index,item in enumerate(nums):
            if item > 0:
                result.append(index+1)
        return result
        
s = Solution()
print s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
                