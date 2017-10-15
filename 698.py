#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:49:55 2017

@author: zhangchi
"""

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 1:
            return True
        
        if len(nums) < k:
            return False
        
        count = 0
        dic = {}
        for item in nums:
            count += item
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
            
        if count % k != 0:
            return False
        else:
            target = count // k
            
        for item in nums:
            if item > target:
                return False
            
        left = k
        return self.helper(target, left, 0, dic)
        
    def helper(self, target, left, now, dic):
        if now == target:
            if left == 1:
                return True
            else:
                return self.helper(target, left-1, 0, dic)
        else:
            tempList = dic.keys()
            tempList.sort(reverse=True)
            for item in tempList:
                if dic[item] > 0:
                    temp = now + item
                    if temp <= target:
                        tempDic = {}
                        for thing in dic:
                            if dic[thing] > 0:
                                tempDic[thing] = dic[thing]
                        tempDic[item] -= 1
                        result = self.helper(target, left, temp, tempDic)
                        if result is True:
                            return True
            return False
        
s = Solution()
print s.canPartitionKSubsets([730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908],4)
#print s.canPartitionKSubsets([85,35,40,64,86,45,63,16,5364,110,5653,97,95],7)
            
            