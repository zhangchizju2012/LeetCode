#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:05:04 2017

@author: zhangchi
"""

class Solution(object):
    # 抓住item是1到n的性质，刚好可以作为index
    # 很像Linked List Cycle II
    # 难在怎么把这个item想成index
    # by solution: https://discuss.leetcode.com/topic/25913/my-easy-understood-solution-with-o-n-time-and-o-1-space-without-modifying-the-array-with-clear-explanation
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = nums[0]
        fast = nums[fast]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
s = Solution()
print s.findDuplicate([1,1])