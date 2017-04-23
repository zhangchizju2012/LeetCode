#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:22:37 2017

@author: zhangchi
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = 0
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root)
        return self.result
    
    def helper(self, root):
        #if root is not None:
        if root.left is not None:
            left = self.helper(root.left)
        else:
            left = 0
        if root.right is not None:
            right = self.helper(root.right)
        else:
            right = 0
        self.result += abs(left-right)
        return left + right + root.val
        