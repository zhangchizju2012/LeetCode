#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:01:54 2017

@author: zhangchi
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tempResult = []
        result = []
        if root is not None:
            tempResult.append(root)
            result.append(tempResult)
        while len(tempResult) > 0:
            resultMiddel = []
            for i in range(len(tempResult)):
                temp = tempResult[i]
                if temp.left is not None:
                    resultMiddel.append(temp.left)
                if temp.right is not None:
                    resultMiddel.append(temp.right)
            if len(resultMiddel) > 0:
                result.append(resultMiddel)
            tempResult = resultMiddel
        final = []
        while len(result) > 0:
            tempFinal = []
            layer = result.pop()
            for item in layer:
                tempFinal.append(item.val)
            final.append(tempFinal)
        return final
#root = None        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.levelOrderBottom(root))