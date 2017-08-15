#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 11:23:01 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        if root is None:
            return 0
        else:
            self.helper(root)
            return self.result - 1 # 减1因为这里是两个node间的间隔距离，而不是总长度
        
    def helper(self, node):
        if node.left is not None:
            left = self.helper(node.left)
        else:
            left = 0
        if node.right is not None:
            right = self.helper(node.right)
        else:
            right = 0
        self.result = max(self.result, left + right + 1)
        return max(left, right) + 1