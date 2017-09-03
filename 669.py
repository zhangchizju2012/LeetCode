#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:51:14 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        self.l = L
        self.r = R
        return self.helper(root)
        
    def helper(self, node):
        if node is None:
            return None
        else:
            if self.l <= node.val <= self.r:
                node.left = self.helper(node.left)
                node.right = self.helper(node.right)
                return node
            else:
                if node.val < self.r:
                    return self.helper(node.right)
                else:
                    return self.helper(node.left)
                
node = TreeNode(1)
node.left = TreeNode(0)
node.right = TreeNode(2)
s= Solution()
result = s.trimBST(node,4,5)