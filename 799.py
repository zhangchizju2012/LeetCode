#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:54:44 2018

@author: zhangchi
"""

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        self.dic = {}
        _, val = self.helper(poured, query_row, query_glass)
        return val
    
    def helper(self, poured, query_row, query_glass):
        if query_row == 0:
            if poured <= 1:
                return 0, poured
            else:
                return poured - 1, 1
        else:
            if (poured, query_row, query_glass) not in self.dic:
                if query_glass > 0:
                    left, _ = self.helper(poured, query_row-1, query_glass-1)
                    left = left / 2.
                else:
                    left = 0
                if query_glass < query_row:
                    right, _ = self.helper(poured, query_row-1, query_glass)
                    right = right / 2.
                else:
                    right = 0
                val = left + right
                if val <= 1:
                    self.dic[(poured, query_row, query_glass)] = [0, val]
                else:
                    self.dic[(poured, query_row, query_glass)] = [val - 1, 1]
            return self.dic[(poured, query_row, query_glass)]

# =============================================================================
# class Solution(object):
#     def champagneTower(self, poured, query_row, query_glass):
#         """
#         :type poured: int
#         :type query_row: int
#         :type query_glass: int
#         :rtype: float
#         """
#         
#         _, val = self.helper(poured, query_row, query_glass)
#         return val
#     
#     def helper(self, poured, query_row, query_glass):
#         if query_row == 0:
#             if poured <= 1:
#                 return 0, poured
#             else:
#                 return poured - 1, 1
#         else:
#             if query_glass > 0:
#                 left, _ = self.helper(poured, query_row-1, query_glass-1)
#                 left = left / 2.
#             else:
#                 left = 0
#             if query_glass < query_row:
#                 right, _ = self.helper(poured, query_row-1, query_glass)
#                 right = right / 2.
#             else:
#                 right = 0
#             val = left + right
#             if val <= 1:
#                 return 0, val
#             else:
#                 return val - 1, 1
# =============================================================================
            
s = Solution()
print(s.champagneTower(6,2,0))
print(s.champagneTower(100,85,39))