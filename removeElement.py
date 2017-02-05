#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 01:41:07 2016

@author: zhangchi
"""

class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] == val:
                pass
            else:
                nums[index] = nums[i]
                index = index + 1
        return index

        '''
    def removeElement(self,  A, elem):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # write your code here
        j = len(A)-1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j+1
        '''
S = Solution()
print S.removeElement([3,2,2,3],3)