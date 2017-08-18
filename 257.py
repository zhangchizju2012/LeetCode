#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:48:43 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        else:
            return self.helper(root)
    
    def helper(self, node):
        label = False
        if node.left is not None:
            left = self.helper(node.left)
            label = True
        else:
            left = []
        if node.right is not None:
            right = self.helper(node.right)
            label = True
        else:
            right = []
        if label:
            result = []
            for item in left+right:
                result.append(str(node.val)+'->'+item)
            return result
        else:
            return [str(node.val)]
            
        