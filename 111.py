#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:32:06 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            now = [root]
            future = []
            count = 1
            while len(now) > 0 or len(future) > 0:
                if len(now) == 0:
                    now = future
                    future = []
                    count += 1
                point = now.pop()
                if point.left is not None:
                    future.append(point.left)
                if point.right is not None:
                    future.append(point.right)
                if point.left is None and point.right is None:
                    return count
        