#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:20:35 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
            return None
        else:
            middle = length // 2
            node = TreeNode(nums[middle])
            left = self.sortedArrayToBST(nums[:middle])
            right = self.sortedArrayToBST(nums[middle+1:])
            node.left = left
            node.right = right
            return node
            
s = Solution()
result = s.sortedArrayToBST([1,2])