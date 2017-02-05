#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 22:10:48 2016

@author: zhangchi
"""

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.results = []
        if not root:
            return self.results
        q = [root]
        while q:
            new_q = []
            for i in q:
                temp = i.val
            self.results.append(temp)
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return self.results