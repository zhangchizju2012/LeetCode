#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 13:45:23 2017

@author: zhangchi
"""

class Solution(object):
    # 看了https://discuss.leetcode.com/topic/35494/solution-explanation的example写出来的
    # 没有看他的代码，只看了他的例子，代码是自己写的
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        length = len(nums)
        index = 0
        scope = 1
        count = 0
        while scope <= n:
            if index >= length or scope < nums[index]:
                count += 1
                scope += scope
            else:
                scope += nums[index]
                index += 1
        return count,scope
                
#==============================================================================
#     # 错了， 我的思路是先找出所有的组合，然后把最大的间距给填上，然后再找出所有的组合，再把最大的间距填上，但这样是错的
#     def minPatches(self, nums, n):
#         """
#         :type nums: List[int]
#         :type n: int
#         :rtype: int
#         """
#         theSet = self.helper(nums)
#         count = 0
#         while len(theSet) < n + 1:
#             #print theSet
#             print count
#             tempList = list(theSet)#.sort()
#             tempList.sort()
#             tempList.append(n+1)
#             largestMargin = -float('inf')
#             previous = tempList[0]
#             for i in xrange(1,len(tempList)):
#                 tempMargin = tempList[i] - previous
#                 largestMargin = max(largestMargin,tempMargin)
#                 previous = tempList[i]
#             if largestMargin > 1:
#                 print largestMargin
#                 count += 1
#                 tempTheSet = set(theSet)
#                 for item in tempTheSet:
#                     theSet.add(item+largestMargin-1)
#         return count
#         
#     def helper(self, nums):
#         if len(nums) > 1:
#             temp = self.helper(nums[1:])
#             returnTemp = set(temp)
#             for item in temp:
#                 returnTemp.add(item+nums[0])
#             return returnTemp
#         elif len(nums) == 1:
#             temp = set()
#             temp.add(0)
#             temp.add(nums[0])
#             return temp
#         else:
#             return set([0])
#==============================================================================
                
s = Solution()
print s.minPatches([],6)