#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:38:17 2016

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getValue(self,tree):
        if tree is not None:
            label_left, left = self.getValue(tree.left)
            middle = tree.val
            label_right, right = self.getValue(tree.right)
            if left is not None and right is not None:
                if label_left and label_right and middle > left[1] and middle < right[0]:
                    return True, [left[0],right[1]]
                else:
                    return False, None
            elif left is None and right is not None:
                if label_left and label_right and middle < right[0]:
                    return True, [middle,right[1]]
                else:
                    return False, None
            elif left is not None and right is None:
                if label_left and label_right and middle > left[1]:
                    return True, [left[0],middle]
                else:
                    return False, None
            else:
                return label_left and label_right, [middle,middle]
        else:
            return True, None
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result,_ = self.getValue(root)
        return result
'''        
tree = TreeNode(5)
tree.left = TreeNode(2)
tree.right = TreeNode(8)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(9)
'''
tree = TreeNode(3)
tree.right = TreeNode(30)
tree.right.left = TreeNode(10)
tree.right.left.right = TreeNode(15)
tree.right.left.right.right = TreeNode(45)

S = Solution()
print S.isValidBST(tree)
    
