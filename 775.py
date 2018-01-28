#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 19:51:38 2018

@author: zhangchi
"""

class Solution(object):
    # 转述一下要求，其实就是：每个数，只能比其临接的左边的数小（当然大爷可以），不能比再左边的数小了
    # 所以可以把扫描到每个位置时的最大值先都存在temp里
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        temp = []
        largest = A[0]
        for item in A:
            largest = max(largest, item)
            temp.append(largest)
        for i in range(2,length):
            if A[i] < temp[i-2]:
                return False
        return True
    
# =============================================================================
#     def isIdealPermutation(self, A):
#         """
#         :type A: List[int]
#         :rtype: bool
#         """
#         length = len(A)
#         i = 0
#         largest = A[0]
#         while i < length - 1:
#             if A[i+1] > A[i]:
#                 largest = A[i+1]
#             else:
#                 if A[i] == largest:
#                     pass
#                 else:
#                     return False
#             i += 1
#         return True
# =============================================================================
    
s = Solution()
print s.isIdealPermutation([1])