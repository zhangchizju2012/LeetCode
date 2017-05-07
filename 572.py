#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 10:10:35 2017

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
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            return []
        else:
            temp = []
            temp.append(s)
            while len(temp) > 0:
                point = temp.pop()
                if point.val == t.val:
                    if self.preorderTraversal(point) == self.preorderTraversal(t):
                        return True
                if point.right is not None:
                    temp.append(point.right)
                if point.left is not None:
                    temp.append(point.left)
            return False
        
point = TreeNode(3)
point.left = TreeNode(4)
point.right = TreeNode(5)
point.left.left = TreeNode(1)
point.left.right = TreeNode(2)

point2 = TreeNode(4)
point2.left = TreeNode(1)
point2.right = TreeNode(2)
#==============================================================================
# point = TreeNode(1)
# point.left = TreeNode(2)
# point.right = TreeNode(3)
# 
# point2 = TreeNode(2)
# point2.left = TreeNode(3)
#==============================================================================
s = Solution()
print s.isSubtree(point,point)