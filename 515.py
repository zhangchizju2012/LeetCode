#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 00:50:42 2017

@author: zhangchi
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        node = [root]
        while len(node) > 0:
            tempResult = -float('inf')
            temp = []
            while len(node):
                n = node.pop()
                if n.right is not None:
                    temp.append(n.right)
                if n.left is not None:
                    temp.append(n.left)
                tempResult = max(tempResult,n.val)
            node = temp
            result.append(tempResult)
        return result