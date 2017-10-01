#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 19:46:39 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.result = 1
        self.helper(root)
        return self.result - 1
        
    def helper(self, node):
        leftCount, leftValue = None, None
        rightCount, rightValue = None, None
        count = 1
        if node.left is not None:
            leftCount, leftValue = self.helper(node.left)
            if leftValue == node.val:
                count += leftCount
        if node.right is not None:
            rightCount, rightValue = self.helper(node.right)
            if rightValue == node.val:
                count += rightCount
        self.result = max(self.result, count)
        if leftValue == rightValue == node.val:
            return 1 + max(leftCount, rightCount), node.val
        elif leftValue == node.val:
            return 1 + leftCount, node.val
        elif rightValue == node.val:
            return 1 + rightCount, node.val
        else:
            return 1, node.val
        
node = TreeNode(1)
node.left = TreeNode(4)
node.right = TreeNode(5)
node.left.left = TreeNode(4)
node.left.right = TreeNode(4)
node.right.right = TreeNode(5)
        
# =============================================================================
# node = TreeNode(5)
# node.left = TreeNode(4)
# node.right = TreeNode(5)
# node.left.left = TreeNode(1)
# node.left.right = TreeNode(1)
# node.right.right = TreeNode(5)
# =============================================================================
s = Solution()
print s.longestUnivaluePath(node)