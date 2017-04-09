#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 23:53:35 2017

@author: zhangchi
"""
#==============================================================================
# 549. Binary Tree Longest Consecutive Sequence II 
# Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.
# 
# Especially, this path can be either increasing or decreasing. For example, 
# [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.
# 
# Example 1:
# Input:
#         1
#        / \
#       2   3
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].
# Example 2:
# Input:
#         2
#        / \
#       1   3
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
#==============================================================================

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = 0
        
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.result
        
    def helper(self,node):
        if node is None:
            return 0, 0
        else:
            leftSmall, leftBig = self.helper(node.left)
            rightSmall, rightBig = self.helper(node.right)
            small = 1
            big = 1
            if node.left is not None:
                if node.left.val + 1 == node.val:
                    small = max(small, leftSmall + 1)
                elif node.left.val - 1 == node.val:
                    big = max(big, leftBig + 1)
            if node.right is not None:
                if node.right.val + 1 == node.val:
                    small = max(small, rightSmall + 1)
                elif node.right.val - 1 == node.val:
                    big = max(big, rightBig + 1)
            self.result = max(self.result, small + big - 1) 
            # important! the biggest may not include root node.
            return small, big
                
#==============================================================================
# http://www.cnblogs.com/grandyang/p/5252599.html
# 298 [LeetCode] Binary Tree Longest Consecutive Sequence 二叉树最长连续序列
#  
# 
# Given a binary tree, find the length of the longest consecutive sequence path.
# 
#  
# 
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
# 
# For example,
# 
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
# 
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
#==============================================================================
        
#==============================================================================
# class Solution(object):
#     def longestConsecutive(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None:
#             return 0
#         left = self.helper(root.left,1,root.val)
#         right = self.helper(root.right,1,root.val)
#         return max(left,right)
#         
#     def helper(self,node,count,value):
#         if node is None:
#             return count
#         elif node.val != value + 1:
#             left = self.helper(node.left,1,node.val)
#             right = self.helper(node.right,1,node.val)
#             return max(left,right)
#         else:
#             left = self.helper(node.left,count+1,node.val)
#             right = self.helper(node.right,count+1,node.val)
#             return max(left,right)
#         
# s = Solution()
# print s.longestConsecutive()
#==============================================================================

# [6,null,9,7,10,null,null,null,11]
# [1,2,4,3,null,5,6,null,null,null,null,7]


