#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:57:26 2017

@author: zhangchi
"""

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.history = []
        self.direction = []
        if root is not None:
            self.history.append(root)
            while root.left is not None:
                self.history.append(root.left)
                self.direction.append('left')
                root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.history) == 0

    def next(self):
        """
        :rtype: int
        """
        value = self.history[-1].val
        if self.direction[-1] == "left":
            
        