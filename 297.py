#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:31:48 2017

@author: zhangchi
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        temp = []
        from Queue import Queue
        q = Queue()
        if root is not None:
            q.put(root)
            temp.append(str(root.val))
        else:
            temp.append('None')
        while q.empty() is False:
            node = q.get()
            if node.left is not None:
                q.put(node.left)
                temp.append(str(node.left.val))
            else:
                temp.append('None')
            if node.right is not None:
                q.put(node.right)
                temp.append(str(node.right.val))
            else:
                temp.append('None')
        s = ""
        for item in temp:
            s += item + ' '
        return s
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        temp = data.split(' ')[:-1]
        if temp[0] == 'None':
            return None
        else:
            from Queue import Queue
            q = Queue()
            index = 1
            result = TreeNode(int(temp[0]))
            q.put(result)
            while q.empty() is False:
                # 注意引用的概念
                node = q.get()
                if temp[index] != 'None':
                    node.left = TreeNode(int(temp[index]))
                    q.put(node.left)
                index += 1
                if temp[index] != 'None':
                    node.right = TreeNode(int(temp[index]))
                    q.put(node.right)
                index += 1
            return result
    
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.right.left = TreeNode(4)
node.right.right = TreeNode(5)
s = Codec()
#print s.serialize(node)
result = s.deserialize("1 2 3 None None 4 5 None None None None ")