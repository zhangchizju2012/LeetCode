#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:16:08 2016

@author: zhangchi
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helpCompare(self,left,right):
        if left is None and right is None:
            return True
        elif left is not None and right is None:
            return False
        elif left is None and right is not None:
            return False
        else:            
            if left.val != right.val:
                return False
            label_out = self.helpCompare(left.left,right.right)
            label_in = self.helpCompare(left.right,right.left)
            return label_out and label_in
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.helpCompare(root.left,root.right)