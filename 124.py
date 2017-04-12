#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:11:25 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = -float('inf')
        
    def maxPathSum(self, root):
        if root is None:
            return 0
        self.helper(root)
        return self.result
        
    def helper(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left = self.helper(root.left)
            right = self.helper(root.right)
            value = root.val
            self.result = max(self.result, left + right + value, left + value, right + value, value)
            return max(left, right, 0) + value