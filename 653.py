#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 19:25:09 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.dic = set()
        self.k = k
        return self.helper(root)
        
    def helper(self, node):
        if node is not None:
            result = self.helper(node.left)
            if result is True:
                return True
            if self.k - node.val in self.dic:
                return True
            else:
                self.dic.add(node.val)
            result = self.helper(node.right)
            if result is True:
                return True
        return False
        