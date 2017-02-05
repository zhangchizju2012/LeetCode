#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:38:42 2016

@author: zhangchi
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is not None and q is None:
            return False
        elif p is None and q is not None:
            return False
        else:            
            if p.val != q.val:
                return False
            label_left = self.isSameTree(p.left,q.left)
            label_right = self.isSameTree(p.right,q.right)
            return label_left and label_right