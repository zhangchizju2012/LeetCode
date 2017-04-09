#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 23:53:35 2017

@author: zhangchi
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.helper(root.left,1,root.val)
        right = self.helper(root.right,1,root.val)
        return max(left,right)
        
    def helper(self,node,count,value):
        if node is None:
            return count
        elif node.val != value + 1:
            left = self.helper(node.left,1,node.val)
            right = self.helper(node.right,1,node.val)
            return max(left,right)
        else:
            left = self.helper(node.left,count+1,node.val)
            right = self.helper(node.right,count+1,node.val)
            return max(left,right)
        
s = Solution()
print s.longestConsecutive()

# [6,null,9,7,10,null,null,null,11]
# [1,2,4,3,null,5,6,null,null,null,null,7]

#==============================================================================
# 549. Binary Tree Longest Consecutive Sequence II My SubmissionsBack To Contest
# User Accepted: 276
# User Tried: 439
# Total Accepted: 280
# Total Submissions: 1048
# Difficulty: Medium
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
