#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 09:29:47 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        else:
            temp = []
            temp.append(root)
            result = []
            while len(temp) > 0:
                point = temp.pop()
                result.append(point.val)
                if point.right is not None:
                    temp.append(point.right)
                if point.left is not None:
                    temp.append(point.left)
            return result
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is not None:
            left = self.inorderTraversal(root.left)
            middel = [root.val]
            right = self.inorderTraversal(root.right)
            return left + middel + right
        else:
            return []
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        a = self.preorderTraversal(s)
        stringA = ""
        for item in a:
            stringA += str(item)
        b = self.preorderTraversal(t)
        stringB = ""
        for item in b:
            stringB += str(item)
        if stringB in stringA is False:
            return False
        else:
            a = self.inorderTraversal(s)
            stringA = ""
            for item in a:
                stringA += str(item)
            b = self.inorderTraversal(t)
            stringB = ""
            for item in b:
                stringB += str(item)
            return stringB in stringA
        
#==============================================================================
# point = TreeNode(3)
# point.left = TreeNode(4)
# point.right = TreeNode(5)
# point.left.left = TreeNode(1)
# point.left.right = TreeNode(2)
# point.left.right.left = TreeNode(0)
# 
# point2 = TreeNode(4)
# point2.left = TreeNode(1)
# point2.right = TreeNode(2)
#==============================================================================
point = TreeNode(1)
point.left = TreeNode(2)
point.right = TreeNode(3)

point2 = TreeNode(2)
point2.left = TreeNode(3)
s = Solution()
print s.isSubtree(point,point2)