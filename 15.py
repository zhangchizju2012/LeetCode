#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 00:13:03 2017

@author: zhangchi
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = {}
        nums.sort()
        if len(nums) >= 1:
            previous = nums[0]
            count = 1
            countList = []
            itemList = []
            for i in xrange(1,len(nums)):
                if nums[i] != previous:
                    countList.append(count)
                    itemList.append(previous)
                    previous = nums[i]
                    count = 1
                else:
                    count += 1
            countList.append(count)
            itemList.append(previous)
            nums = []
            for a,b in zip(itemList,countList):
                if a != 0:
                    # 非0的数超过2次没有意义
                    nums += [a] * min(b,2)
                else:
                    # 0的数超过1次没有意义，当然出现3次还是可以作为答案的
                    if b <= 2:
                        nums += [0]
                    else:
                        result[(0,0,0)] = 1
                        nums += [0]
             
        for i in xrange(len(nums)-2):
            target = -nums[i]
            dic = {}
            for j in xrange(i+1,len(nums)):
                # 中间这里就当做2sum处理，也是用hashmap
                if target - nums[j] in dic:
                    if (-target,target - nums[j],nums[j]) not in result:
                        result[(-target,target - nums[j],nums[j])] = 1
                dic[nums[j]] = 1
        return [list(item) for item in result.keys()]
                
#==============================================================================
#     def threeSum(self, nums):
#         # original version, also works, but slower
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         result = {}
#         for i in xrange(len(nums)-2):
#             target = -nums[i]
#             dic = {}
#             for j in xrange(i+1,len(nums)):
#                 if target - nums[j] in dic:
#                     if (-target,target - nums[j],nums[j]) not in result:
#                         result[(-target,target - nums[j],nums[j])] = 1
#                 dic[nums[j]] = 1
#         return [list(item) for item in result.keys()]
#==============================================================================
        
s = Solution()
print s.threeSum([-1, 0, 1, 2, -1,-1, -4])