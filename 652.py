#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 19:30:09 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 自己写的，比赛题
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if root is None:
            return []
        self.result = []
        self.dict = {}
        self.helper(root)
        return self.result
    
    def helper(self, root):
        if root.left is not None:
            left = self.helper(root.left)
        else:
            left = ['left'] 
            # 左右是None的情况要区分一下，不然[0,null,0]和[0,0,null]写成list无法区分
            # 都是[None, 1, None, 1, None]
        if root.right is not None:
            right = self.helper(root.right)
        else:
            right = ['right']
        here = left + [root.val] + right
        tupleVesrion = tuple(here)
        if tupleVesrion in self.dict:
            if self.dict[tupleVesrion] == 1:
                self.result.append(root)
                self.dict[tupleVesrion] += 1
            else:
                self.dict[tupleVesrion] += 1
        else:
            self.dict[tupleVesrion] = 1
        return here

s = Solution()
node = TreeNode(0)
node.left = TreeNode(0)
node.right = TreeNode(0)
node.left.left = TreeNode(0)
node.right.right = TreeNode(0)
#node.right.right.right = TreeNode(0)
result = s.findDuplicateSubtrees(node)

#[1,2,3,4,null,2,4,null,null,4]