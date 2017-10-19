#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:16:29 2017

@author: zhangchi
"""

class Solution(object):
    # dfs
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        self.dic = set()
        for item in bank:
            self.dic.add(item)
        diff = set()
        same = set()
        for index in xrange(len(start)):
            if start[index] != end[index]:
                diff.add(index)
            else:
                same.add(index)
        return self.helper(diff, same, start, end, 0)
                
    def helper(self, diff, same, start, end, count):
        if len(diff) == 0:
            return count
        for item in diff:
            change = start[:item] + end[item] + start[item+1:]
            if change in self.dic:
                diffChange = set(diff)
                diffChange.remove(item)
                countTotal = self.helper(diffChange, same, change, end, count + 1)
                if countTotal > 0:
                    return countTotal
        for item in same:
            for temp in ["A","T","C","G"]:
                if temp != end[item]:
                    change = start[:item] + temp + start[item+1:]
                    if change in self.dic:
                        diffChange = set(diff)
                        diffChange.add(item)
                        sameChange = set(same)
                        sameChange.remove(item)
                        countTotal = self.helper(diffChange, sameChange, change, end, count + 1)
                        if countTotal > 0:
                            return countTotal
        return -1
    
s = Solution()
start = "AACCGGTT"
end =   "AAACGGTA"
bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]
print s.minMutation(start,end,bank)


# =============================================================================
# class Solution(object):
#     def minMutation(self, start, end, bank):
#         """
#         :type start: str
#         :type end: str
#         :type bank: List[str]
#         :rtype: int
#         """
#         self.dic = set()
#         for item in bank:
#             self.dic.add(item)
#         diff = set()
#         for index in xrange(len(start)):
#             if start[index] != end[index]:
#                 diff.add(index)
#         return self.helper(diff, start, end, 0)
#                 
#     def helper(self, diff, start, end, count):
#         if len(diff) == 0:
#             return count
#         for item in diff:
#             change = start[:item] + end[item] + start[item+1:]
#             if change in self.dic:
#                 diffChange = set(diff)
#                 diffChange.remove(item)
#                 countTotal = self.helper(diffChange, change, end, count + 1)
#                 if countTotal > 0:
#                     return countTotal
#         return -1
# =============================================================================
