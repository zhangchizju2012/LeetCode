#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 14:28:26 2016

@author: zhangchi
"""

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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.dictionary = {}
        self.helpZigzag(root,0)
        result = []
        for item in self.dictionary:
            result.append(self.dictionary[item])
        return result