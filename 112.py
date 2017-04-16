#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 22:51:31 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        else:
            if root.left is not None:
                if self.hasPathSum(root.left, sum - root.val) == True:
                    return True
            if root.right is not None:
                if self.hasPathSum(root.right, sum - root.val) == True:
                    return True
            elif root.left is None:
                if root.val == sum:
                    return True
                else:
                    return False
            return False
            
        