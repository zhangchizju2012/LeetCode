#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 01:22:14 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) > 0:
            position = inorder.index(postorder[-1])
            node = TreeNode(postorder[-1])
            node.left = self.buildTree(inorder[:position],postorder[:position])
            node.right = self.buildTree(inorder[position+1:],postorder[position:-1])
            return node
        else:
            return None