#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 12:00:54 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.helper(root)
    
    def helper(self, node):
        leftStart = None
        rightStart = None
        if node.left is not None:
            leftStart, leftEnd = self.helper(node.left)
        if node.right is not None:
            rightStart, rightEnd = self.helper(node.right)
        # 后面进行节点的串联
        if leftStart is not None:
            node.left = None  # 不要忘了
            node.right = leftStart
            if rightStart is not None:
                leftEnd.left = None # 不要忘了
                leftEnd.right = rightStart
                return node, rightEnd
            else:
                return node, leftEnd
        else:
            if rightStart is not None:
                node.left = None  # 不要忘了
                node.right = rightStart
                return node, rightEnd
            else:
                return node, node
        