#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 00:46:20 2017

@author: zhangchi
"""
# http://www.programcreek.com/2012/12/leetcode-solution-of-iterative-binary-tree-postorder-traversal-in-java/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result =[]
        stack = []
        stack.append(root)
        while len(stack) > 0:
            peek = stack[-1]
            if peek.right is None and peek.left is None:
                result.append(peek.val)
                stack.pop()
            if peek.right is not None:
                stack.append(peek.right)
                peek.right = None
            if peek.left is not None:
                stack.append(peek.left)
                peek.left = None
        return result
        
node = TreeNode(1)
node.right = TreeNode(2)
s = Solution()
print s.postorderTraversal(node)