#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:01:54 2017

@author: zhangchi
"""
import copy
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
            saveTempResult = copy.deepcopy(tempResult)
            result.append(saveTempResult)
        label = True
        while label:
            resultMiddel = []
            label = False
            while len(tempResult) > 0:
                temp = tempResult.pop(0)
                if temp.left is not None:
                    resultMiddel.append(temp.left)
                if temp.right is not None:
                    resultMiddel.append(temp.right)
                label = True
            saveResultMiddel = copy.deepcopy(resultMiddel)
            if len(saveResultMiddel) > 0:
                result.append(saveResultMiddel)
            tempResult = resultMiddel
        final = []
        while len(result) > 0:
            tempFinal = []
            layer = result.pop()
            for item in layer:
                tempFinal.append(item.val)
            final.append(tempFinal)
        return final
root = None        
#==============================================================================
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
#==============================================================================
s = Solution()
print(s.levelOrderBottom(root))