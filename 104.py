#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:14:54 2016

@author: zhangchi
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        self.helpDepth(root,1)
        return self.depth
    def helpDepth(self,root,i):
        if root is not None:
            self.depth = max(self.depth,i)
            self.helpDepth(root.left,i+1)
            self.helpDepth(root.right,i+1)
            return
        else:
            return