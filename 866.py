#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 18:16:14 2018

@author: zhangchi
"""

# 包含了所有最长的路径的最近母节点

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node, _ = self.helper(root)
        return node
    
    def helper(self, node):
        leftDepth = 0
        rightDepth = 0
        if node.left is not None:
            leftNode, leftDepth = self.helper(node.left)
        if node.right is not None:
            rightNode, rightDepth = self.helper(node.right)
        if leftDepth == rightDepth == 0: # 其实跟下面重复了，不过方便理解
            return node, 1
        else:
            if leftDepth > rightDepth:
                return leftNode, leftDepth + 1
            elif rightDepth > leftDepth:
                return rightNode, rightDepth + 1
            else:
                return node, leftDepth + 1
            