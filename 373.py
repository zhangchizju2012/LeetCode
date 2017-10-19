#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 17:29:33 2017

@author: zhangchi
"""

class Solution(object):
    # heap, very similar to 2D matrix
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        heap = []
        count = 0
        total = 1
        length1 = len(nums1)
        length2 = len(nums2)
        while count < min(k,length1*length2):
            # 2D matrix process
            for i in range(total):
                if i < length1 and total-1-i < length2:
                    heapq.heappush(heap,(nums1[i]+nums2[total-1-i],i,total-1-i))
                    count += 1
            total += 1
        count = 0
        result = []
        while count < min(k,length1*length2):
            temp = heapq.heappop(heap)
            result.append([nums1[temp[1]],nums2[temp[2]]])
            count += 1
        return result

#==============================================================================
# class Solution(object):
#     # heap, very similar to 2D matrix
#     # wrong
#     def kSmallestPairs(self, nums1, nums2, k):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         import heapq
#         heap = []
#         count = 0
#         index = 0
#         length1 = len(nums1)
#         length2 = len(nums2)
#         while count < min(k,length1*length2):
#             # 2D matrix process
#             if index < length2:
#                 for i in xrange(min(index,length1-1)):
#                     heapq.heappush(heap,(nums1[i]+nums2[index],i,index))
#                     count += 1
#             if index < length1:
#                 for i in xrange(min(index,length2-1)):
#                     heapq.heappush(heap,(nums1[index]+nums2[i],index,i))
#                     count += 1
#             if index < length1 and index < length2:
#                 heapq.heappush(heap,(nums1[index]+nums2[index],index,index))
#                 count += 1
#             index += 1
#         count = 0
#         result = []
#         while count < min(k,length1*length2):
#             temp = heapq.heappop(heap)
#             result.append([nums1[temp[1]],nums2[temp[2]]])
#             count += 1
#         return result
#==============================================================================
        
#==============================================================================
#     def kSmallestPairs(self, nums1, nums2, k):
#         # wrong
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         length1 = len(nums1)
#         length2 = len(nums2)
#         index1 = 0
#         index2 = 0
#         count = 0
#         result = []
#         while count < min(k,length1*length2):
#             result.append([nums1[index1],nums2[index2]])
#             count += 1
#             if index1 < length1 - 1 and index2 < length2 - 1:
#                 if nums1[index1] + nums2[index2+1] < nums1[index1+1] + nums2[index2]:
#                     index2 += 1
#                 else:
#                     index1 += 1
#             elif index1 == length1 - 1 and index2 < length2 - 1:
#                 index2 += 1
#             else:
#                 index1 += 1
#         return result
#==============================================================================
        
s = Solution()
print s.kSmallestPairs([-10,-4,0,0,6],[3,5,6,7,8,100],10)