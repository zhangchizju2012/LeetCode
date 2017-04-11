#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:20:56 2017

@author: zhangchi
"""

#==============================================================================
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#==============================================================================

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
        # only in case of the tree does not exist, other time will not come here
            return []
        else:
            if root.left is None and root.right is None:
                if root.val == sum:
                    return [[root.val]]
                else:
                    return []
            elif root.left is not None and root.right is not None:
                left = self.pathSum(root.left, sum - root.val)
                right = self.pathSum(root.right, sum - root.val)
            elif root.left is not None:
                left = self.pathSum(root.left, sum - root.val)
                right = []
            elif root.right is not None:
                left = []
                right = self.pathSum(root.right, sum - root.val)
            leftNew = []
            rightNew = []
            if left != []:
                for item in left:
                    leftNew.append([root.val] + item)
            if right != []:
                for item in right:
                    rightNew.append([root.val] + item)
            if leftNew != [] and rightNew != []:
                return leftNew + rightNew
            elif leftNew != []:
                return leftNew
            elif rightNew != []:
                return rightNew
            else:
                return []
        
        
        
#[5,4,8,11,null,13,4,null,2,null,null,5,1]
#22
            