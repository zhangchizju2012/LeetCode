#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:59:01 2017

@author: zhangchi
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        a = 0
        b = 0
        count = 0
        while a < m + count and b < n:
            if nums1[a] < nums2[b]:
                a += 1
            else:
                nums1[a+1:] = nums1[a:-1]
                nums1[a] = nums2[b]
                b += 1
                a += 1
                count += 1
        for item in nums2[b:]:
            nums1[a+1:] = nums1[a:-1]
            nums1[a] = item
            a += 1
        return nums1
    
s = Solution()
#print s.merge([1,2,4,8,0,0,0,0,0,0],4,[2,3,6,9],4)
print s.merge([4,0,0,0,0,0],1,[2,3,6,9],4)

#==============================================================================
# notes:
# a = [1,2,3,4,5]
# 
# a[3:] = a[2:-1]
# 
# a
# Out[45]: [1, 2, 3, 3, 4]
# a[3:]
# Out[46]: [3, 4]
# 
# a = [1,2,3,4,5]
# 
# a[2:-1] = a[3:]
# 
# a
# Out[49]: [1, 2, 4, 5, 5]
#==============================================================================
