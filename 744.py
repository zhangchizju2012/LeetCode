#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:30:30 2017

@author: zhangchi
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target and letters[mid-1] <= target:
                return letters[mid]
            elif letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[0]
    
s = Solution()
print s.nextGreatestLetter(["c", "f", "j"],"k")