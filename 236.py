#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Edited on Wed Jul 12 12:41:02 2017

@author: zhangchi
"""

# 复习

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root, p, q)
    
    def helper(self,node, p, q):
        # 要考虑p和q是存在于一边还是两边的问题
        if node == p or node == q:
            return node
        else:
            if node.left is not None:
                left = self.helper(node.left, p, q) # 如果左边不存在，只可能存在于右边或者不存在（存在于另一分支）
            else: # 到底了
                left = None
            if node.right is not None:
                right = self.helper(node.right, p, q)
            else:
                right = None
            if left is None and right is None:
                return None
            else:
                if left is None:
                    return right
                elif right is None:
                    return left
                else:
                    return node
                
        

"""
Created on Fri May 26 01:30:52 2017

@author: zhangchi
"""
# 下面的效率比较低，没有AC，但是思路也是不错的

#==============================================================================
# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         self.p = p
#         self.q = q
#         self.result = []
#         self.findPosition(root,[])
#         final = root
#         for a,b in zip(self.result[0],self.result[1]):
#             if a == b:
#                 if a == 'left':
#                     final = final.left
#                 elif a == 'right':
#                     final = final.right
#             else:
#                 return final
#         return final
#                 
#     def findPosition(self, node, path):
#         if len(self.result) < 2:
#             if node is not None:
#                 if node == self.p or node == self.q:
#                     self.result.append(path)
#                 self.findPosition(node.left,path+['left'])
#                 self.findPosition(node.right,path+['right'])
#==============================================================================
                
node = TreeNode(3)
node.left = TreeNode(5)
node.right = TreeNode(1)
node.left.left = TreeNode(6)
node.left.right = TreeNode(2)
node.right.left = TreeNode(0)
node.right.right = TreeNode(8)
node.left.right.left = TreeNode(7)
node.left.right.right = TreeNode(4)
s = Solution()
print s.lowestCommonAncestor(node,node.left,node.right).val

#==============================================================================
# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         pass
#     def checkExist(self, root, point):
#         if root is None:
#             return False
#         from Queue import Queue
#         q = Queue()
#         q.put(root)
#         while q.empty() == False:
#             temp = q.get()
#==============================================================================


        