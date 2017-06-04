#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:30:25 2017

@author: zhangchi
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        else:
            nums.sort()
            itemList = []
            countList = []
            previous = nums[0]
            count = 1
            for i in xrange(1,len(nums)):
                if nums[i] != previous:
                    itemList.append(previous)
                    countList.append(min(count,3))
                    count = 1
                    previous = nums[i]
                else:
                    count += 1
            itemList.append(previous)
            countList.append(min(count,3))
            nums = []
            for a,b in zip(itemList,countList):
                nums += [a] * b

            result = float('inf')
            for i in xrange(len(nums)-2):
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    temp = nums[i] + nums[left] + nums[right]
                    if temp == target:
                        return temp
                    if abs(temp-target) < abs(result-target):
                        result = temp
                    if temp < target:
                        left += 1
                    else:
                        right -= 1
            return result
    # 排序并删掉没用的元素之后 三个三个扫描过去 错！ 很多组合被忽略了
#==============================================================================
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if len(nums) < 3:
#             return 0
#         else:
#             nums.sort()
#             itemList = []
#             countList = []
#             previous = nums[0]
#             count = 1
#             for i in xrange(1,len(nums)):
#                 if nums[i] != previous:
#                     itemList.append(previous)
#                     countList.append(min(count,3))
#                     count = 1
#                     previous = nums[i]
#                 else:
#                     count += 1
#             itemList.append(previous)
#             countList.append(min(count,3))
#             nums = []
#             for a,b in zip(itemList,countList):
#                 nums += [a] * b
#             previous = sum(nums[:3])
#             if previous >= target:
#                 return previous
#             for i in xrange(1,len(nums)-2):
#                 now = sum(nums[i:i+3])
#                 if now > target:
#                     if abs(now-target) < abs(previous-target):
#                         return now
#                     else:
#                         return previous
#                 else:
#                     previous = now
#             return previous
#==============================================================================
            
s = Solution()
print s.threeSumClosest([0,2,1,-3],1)