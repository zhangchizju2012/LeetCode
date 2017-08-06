#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 19:40:13 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        else:
            maxValue = max(nums)
            index = nums.index(maxValue)
            node = TreeNode(maxValue)
            node.left = self.constructMaximumBinaryTree(nums[:index])
            node.right = self.constructMaximumBinaryTree(nums[index+1:])
            return node
        
    
    
        