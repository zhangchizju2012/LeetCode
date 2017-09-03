#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:29:19 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left is None and root.right is None:
            return -1
        else:
            if root.left.val != root.right.val:
                if root.left.val == root.val:
                    left = self.findSecondMinimumValue(root.left)
                    right = root.right.val
                    if left != -1:
                        return min(left,right)
                    else:
                        return right
                else:
                    left = root.left.val
                    right = self.findSecondMinimumValue(root.right)
                    if right != -1:
                        return min(left,right)
                    else:
                        return left
            else:
                left = self.findSecondMinimumValue(root.left)
                right = self.findSecondMinimumValue(root.right)
                if left == -1 and right == -1:
                    return -1
                elif left == -1:
                    return right
                elif right == -1:
                    return left
                else:
                    return min(left,right)
                

# [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]
node = TreeNode(2)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.right.left = TreeNode(5)
node.right.right = TreeNode(7)
s = Solution()
print s.findSecondMinimumValue(node)

        