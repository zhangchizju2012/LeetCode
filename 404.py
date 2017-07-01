#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 18:29:30 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        if root is not None:
            self.helper(root,False)
        return self.result
        
    def helper(self,node,label):
        if node.left is None and node.right is None and label:#label用来指示是否为左节点
            self.result += node.val
        else:
            if node.left is not None:
                self.helper(node.left,True)
            if node.right is not None:
                self.helper(node.right,False)
            
            