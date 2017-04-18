#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:17:21 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        return self.pathSum(root.left, sum) + self.pathSum(root.right, sum) + self.helper(root, sum)

    def helper(self, root, sum):
        if root is None:
            return 0
        else:
            temp = 0
            if root.val == sum:
                temp = 1
            return temp + self.helper(root.left, sum-root.val) + self.helper(root.right, sum-root.val)
            
            
#==============================================================================
# [10,5,-3,3,2,null,11,3,-2,null,1]
# 8
#==============================================================================
