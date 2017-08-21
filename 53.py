#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Reviewed on Sun Aug 20 22:24:44 2017

@author: zhangchi
"""
class Solution(object):
    # DP
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [-float('inf')] # 每个元素表示，以这个元素为终止，最大值是多少
        for item in nums:
            if result[-1] < 0: # 如果前面的是负的，最大值就是本身
                result.append(item)
            else:
                result.append(item+result[-1])
        return max(result)
        

S = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print S.maxSubArray(nums)
# =============================================================================
# class Solution(object):
#     # 分治
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         length = len(nums)
#         if length == 1:
#             return nums[0]
#         left = self.maxSubArray(nums[:length/2])
#         right = self.maxSubArray(nums[length/2:])
#         leftValue, leftCount = self.helper(nums[:length/2][::-1])
#         rightValue, rightCount = self.helper(nums[length/2:])
#         if leftCount == rightCount == 0:#至少得有一个数
#             middle = max(nums[length/2-1],nums[length/2])
#         else:
#             middle = leftValue + rightValue
#         return max(left,right,middle)
#         
#     def helper(self,nums):
#         # 计算含有一端时的最大值
#         count = 0
#         value = 0
#         maxValue = -float('inf')
#         for index, item in enumerate(nums):
#             value += item
#             if value > maxValue:
#                 maxValue = value
#                 count = index + 1
#         return maxValue, count
# 
# 
# S = Solution()
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print S.maxSubArray(nums)
# =============================================================================

"""
Created on Fri Dec 16 20:56:53 2016

@author: zhangchi
"""

# =============================================================================
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         length = len(nums)
#         if length == 0:
#             return
#         if length == 1:
#             return nums[0]
#         middle_index = length/2
#         left = self.maxSubArray(nums[:middle_index])
#         right = self.maxSubArray(nums[middle_index:])
#         
#         leftWithMid = 0
#         maxLeftWithMid = 0
#         leftLable = True
#         for i in range(middle_index-1,-1,-1):
#             leftWithMid = leftWithMid + nums[i]
#             if leftWithMid > maxLeftWithMid:
#                 maxLeftWithMid = leftWithMid
#                 leftLable = False
#                 
#         rightWithMid = 0
#         maxRightWithMid = 0
#         rightLabel = True
#         for i in range(middle_index,length):
#             rightWithMid = rightWithMid + nums[i]
#             if rightWithMid > maxRightWithMid:
#                 maxRightWithMid = rightWithMid
#                 rightLabel = False
#         
#         if leftLable and rightLabel:#避免出现一个元素都不取的情况，如[-1,-2]时候
#             value = max(nums[middle_index-1],nums[middle_index])
#         else:
#             value = maxLeftWithMid + maxRightWithMid
#         
#         return max(left,right,value)
#         
# S = Solution()
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print S.maxSubArray(nums)
# =============================================================================
