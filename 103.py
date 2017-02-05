#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:07:53 2016

@author: zhangchi
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helpZigzag(self,root,i):
        if root is not None:
            value = root.val
            if i in self.dictionary:
                self.dictionary[i].append(value)
            else:
                self.dictionary[i] = [value]
            self.helpZigzag(root.left,i+1)
            self.helpZigzag(root.right,i+1)
            return
        else:
            return
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.dictionary = {}
        self.helpZigzag(root,0)
        result = []
        for item in self.dictionary:
            if item%2 == 0:
                result.append(self.dictionary[item])
            else:
                self.dictionary[item].reverse()
                result.append(self.dictionary[item])
        return result

#[3,9,20,null,null,15,7,3,6,4,2,null,2,null,null,1,null,2,3]
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
tree.right.left.left = TreeNode(3)
tree.right.left.right = TreeNode(6)
tree.right.left.left.right = TreeNode(2)
S = Solution()
print S.zigzagLevelOrder(tree)