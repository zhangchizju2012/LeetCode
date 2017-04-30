#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:10:07 2017

@author: zhangchi
"""

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.n = n
        self.dictionary = {}
        for i in range(n):
            self.dictionary[i] = []
        for item in edges:
            self.dictionary[item[0]].append(item[1])
            self.dictionary[item[1]].append(item[0])

        depth = float('inf')
        for i in range(n):
            tempDepth = self.checkDepth(i)
            if tempDepth < depth:
                result = [i]
                depth = tempDepth
            elif tempDepth == depth:
                result.append(i)
        return result
            
    def checkDepth(self,k):
        # bfs
        stack = [k]
        dic = {i:False for i in range(self.n)}
        dic[k] = True
        depth = 0
        while len(stack) > 0:
            depth += 1
            alist = []
            while len(stack) > 0:
                temp = stack.pop()
                for item in self.dictionary[temp]:
                    if dic[item] == False:
                        dic[item] = True
                        alist.append(item)
            stack = alist
        return depth
        
        
s = Solution()
print s.findMinHeightTrees(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])


#==============================================================================
# class Solution(object):
#     def findMinHeightTrees(self, n, edges):
#         """
#         :type n: int
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#         self.dictionary = {}
#         for item in edges:
#             if item[0] in self.dictionary:
#                 self.dictionary[item[0]].append(item[1])
#             else:
#                 self.dictionary[item[0]] = [item[1]]
#             if item[1] in self.dictionary:
#                 self.dictionary[item[1]].append(item[0])
#             else:
#                 self.dictionary[item[1]] = [item[0]]
#         depth = float('inf')
#         for item in self.dictionary:
#             depth = min(depth, self.checkDepth(self.dictionary[item],item))
#         return depth + 1
#         
#     def checkDepth(self, alist, item):
#         depth = 0
#         for a in alist:
#             for thing in self.dictionary[a]:
#                 if thing != item:
#                     depth = max(depth, self.checkDepth(self.dictionary[thing],thing))
#         return depth + 1
#==============================================================================