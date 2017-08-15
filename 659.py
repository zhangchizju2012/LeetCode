#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:34:03 2017

@author: zhangchi
"""
# inspired by
# https://discuss.leetcode.com/topic/99187/java-o-n-time-o-n-space
# 看到这句话We iterate through the array once more and for each element we either see if it can be appended to a previously constructed consecutive sequence or if it can be the start of a new consecutive sequence. If neither are true, then we return false.
# 想到的，但是我的算法跟这个好像也不太相关
# 我的思路：来了新的元素，先将之前短的candidate变长，之前的candidate不够的话就以新元素开头，成为新的candidate
# 之前的candidate多了的话检查多余的candidate的长度是否已经满足要求

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        valueList = []
        for item in nums:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
                valueList.append(item)
        candidates = []
        for item in valueList:
            temp = []
            count = 0
            for candidate in candidates:
                # 越短的先被考虑添加新元素（按照后续的算法line41，已经按长度排好了）
                if item - candidate[-1] == 1 and count < dic[item]:
                    temp.append(candidate+[item])
                    count += 1
                else:#检查剩余的candidate长度是否满足，满足了的话就直接丢弃不用再考虑了
                    if len(candidate) >= 3:
                        pass
                    else:
                        return False
            if count < dic[item]: # 还有剩余的话放到最前头，因为最新添加的最短，后面有新元素应该先被考虑
                temp = [[item] for _ in xrange(dic[item] - count)] + temp
            candidates = temp
        for candidate in candidates:
            if len(candidate) < 3:
                return False
        return True
                    

# =============================================================================
# class Solution(object):
#     def isPossible(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) == 0:
#             return True
#         dic = {}
#         temp = []
#         future = []
#         for index, item in enumerate(nums):
#             if item not in dic:
#                 if len(temp) == 0 or temp[-1] + 1 == item:
#                     dic[item] = 1
#                     temp.append(item)
#                     if len(temp) >= 3:
#                         if self.isPossible(future+nums[index+1:]):
#                             return True
#                 else:
#                     break
#             else:
#                 dic[item] += 1
#                 future.append(item)
#                 if len(temp) >= 3:
#                     if self.isPossible(future+nums[index+1:]):
#                         return True
#         return False
#                 
# =============================================================================
s = Solution()
a = [1,2,3,4,4,5]
#a = [14,14,15,15,16,16,17,17,18,18,19,19,20,20,20,21,21,21,22,22,22,23,23,23,24,24,24,24,25,25,25,25,26,26,26,26,27,27,27,27,28,28,28,28,29,29,29,30,30,30,31,31,31,32,32,32,33,33,33,34,34,34,35,35,35,36,36,36,37,37,37,38,38,38,39,39,39,40,40,40,41,41,41,42,42,43,43,44,44,45,45,46,46,47,47,47,48,48,48,49,49,49,50,50,50,51,51,51,52,52,52,53,53,53,54,54,54,55,55,55,56,56,56,57,57,57,58,58,58,59,59,59,60,60,60,61,61,61,62,62,62,62,63,63,63,63,64,64,64,64,65,65,65,65,65,66,66,66,66,66,67,67,67,67,67,68,68,68,68,68,68,69,69,69,69,69,69,70,70,70,70,70,70,71,71,71,71,71,71,72,72,72,72,72,72,73,73,73,73,73,73,74,74,74,74,74,74,75,75,75,75,75,75,76,76,76,76,76,76,77,77,77,77,77,77,78,78,78,78,78,78,79,79,79,79,79,79,80,80,80,80,80,80,80,81,81,81,81,81,81,81,82,82,82,82,82,82,82,83,83,83,83,83,83,83,84,84,84,84,84,84,84,85,85,85,85,85,85,85,86,86,86,86,86,86,86,86,87,87,87,87,87,87,87,87,88,88,88,88,88,88,88,88,89,89,89,89,89,89,89,89,90,90,90,90,90,90,90,90,91,91,91,91,91,91,91,92,92,92,92,92,92,92,93,93,93,93,93,93,93,94,94,94,94,94,94,95,95,95,95,95,95,96,96,96,96,96,96,97,97,97,97,97,97,98,98,98,98,98,98,99,99,99,99,99,99,100,100,100,100,100,101,101,101,101,101,102,102,102,102,102,103,103,103,103,103,104,104,104,104,104,105,105,105,105,105,106,106,106,106,106,107,107,107,107,107,108,108,108,108,108,109,109,109,109,109,110,110,110,110,110,111,111,111,111,111,112,112,112,113,113,113,114,114,114,115,115,115,116,116,116,117,117,117,118,118,118,119,119,119,120,120,120,121,121,121,122,122,122,123,123,123,124,124,124,125,125,125,126,126,126,127,127,127,128,128,128,129,129,129,130,130,130,131,131,131,132,132,132,133,133,133,134,134,135,135,136,136,137,137,138,138,139,139,140,140,141,141,142,142,143,143,144,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170]
print s.isPossible(a)