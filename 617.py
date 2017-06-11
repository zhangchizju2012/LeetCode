#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 19:31:53 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.helper(t1,t2)
        
    def helper(self, t1, t2):
        if t1 is not None and t2 is not None:
            node = TreeNode(t1.val+t2.val)
            node.left = self.helper(t1.left,t2.left)
            node.right = self.helper(t1.right,t2.right)
            return node
        elif t1 is not None and t2 is None:
            return t1
        elif t1 is None and t2 is not None:
            return t2
        else:
            return None