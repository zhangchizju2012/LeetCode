#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:45:04 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        else:
            return self.helper(root,v,d)
    
    def helper(self,root,v,d):
        if d == 2:
            node = TreeNode(root.val)
            node.left = TreeNode(v)
            node.left.left = root.left
            node.right = TreeNode(v)
            node.right.right = root.right
            return node
        else:
            node = TreeNode(root.val)
            if root.left is not None:
                node.left = self.helper(root.left,v,d-1)
            if root.right is not None:
                node.right = self.helper(root.right,v,d-1)
            return node
            
node = TreeNode(4)
node.left = TreeNode(2)
node.right = TreeNode(6)
node.left.left = TreeNode(3)
node.left.right = TreeNode(1)
node.right.left = TreeNode(5)
s = Solution()
result = s.addOneRow(node,1,10)