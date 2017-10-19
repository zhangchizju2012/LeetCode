#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 00:24:22 2017

@author: zhangchi
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        indexList = []
        for index, item in enumerate(nums):
            if item == 0:
                indexList.append(index)
        indexList.append(len(nums)) # 相当于最后也有个0，配合一下后面的处理
        count = 0
        for i in xrange(len(indexList)-1):
            nums[indexList[i]-count:indexList[i+1]-count-1] = nums[indexList[i]+1:indexList[i+1]]
            count += 1 #每次往后挪动一次，相当于每次有个0的位置被空出来了，所以前面要减掉count，且count每次加一
        for i in xrange(indexList[-1]-count,len(nums)):
            nums[i] = 0
        #return nums
        
s = Solution()
print s.moveZeroes([])