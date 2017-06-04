#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 19:44:46 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = ""
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is not None:
            self.helper(t)
        return self.result
            
    def helper(self,node):
        self.result += str(node.val)
        if node.left is not None:
            self.result += "("
            self.helper(node.left)
            self.result += ")"
        elif node.right is not None:
            self.result += "()"
        if node.right is not None:
            self.result += "("
            self.helper(node.right)
            self.result += ")"
n = TreeNode(1)
n.left = TreeNode(2)
n.right = TreeNode(3)
n.left.left = TreeNode(4)   
s = Solution()
print s.tree2str(n)
            