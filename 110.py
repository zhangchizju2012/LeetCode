#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:48:28 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            if self.helper(root) == False:
                return False
            else:
                return True
    
    def helper(self, node):
        if node.left is not None:
            left = self.helper(node.left)
            if left == False:
                return False
        else:
            left = 0
        if node.right is not None:
            right = self.helper(node.right)
            if right == False:
                return False
        else:
            right = 0
        if abs(right-left) <= 1:
            return max(left,right) + 1
        else:
            return False
        