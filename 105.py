#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 01:00:31 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) > 0:
            position = inorder.index(preorder[0])
            node = TreeNode(preorder[0])
            node.left = self.buildTree(preorder[1:1+position],inorder[:position])
            node.right = self.buildTree(preorder[1+position:],inorder[1+position:])
            return node
        else:
            return None