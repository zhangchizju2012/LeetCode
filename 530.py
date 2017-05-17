#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 00:11:15 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 相当于把有序数组变成BST的逆过程，相当于108的逆过程
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tempResult = self.helper(root)
        result = [tempResult[i+1]-tempResult[i] for i in xrange(len(tempResult)-1)]
        return min(result)
        
    def helper(self, root):
        middle = [root.val]
        if root.left is not None:
            left = self.helper(root.left)
        else:
            left = []
        if root.right is not None:
            right = self.helper(root.right)
        else:
            right = []
        return left + middle + right