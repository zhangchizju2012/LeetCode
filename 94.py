#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:10:31 2016

@author: zhangchi
"""

class Solution(object):
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