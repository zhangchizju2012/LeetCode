#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 19:50:50 2017

@author: zhangchi
"""

class Solution(object):
    # 自己写的，复杂度应该是n^2
    # 看大家的提交记录，应该是有优化算法的
    # 优化算法我其实想到了的 https://discuss.leetcode.com/topic/80793/java-o-n-time-o-k-space
    # 就是从左到右，记录总和（mod过的），如果之前出现过，说明中间有一段就是n倍的k
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            for i in xrange(1,len(nums)):
                if nums[i] == nums[i-1] == 0:
                    return True # nums=[0,0], target=0是可以的 
            return False
        else:
            k = abs(k) # k可以是负的，当成正的处理即可
            dic = {} # dic 储存的是从第1个数到第n个数，第2个数到第n个数，第n-1到第n个数，求和的可能性(除掉了k，使数量减少)
            for item in nums:
                temp = item % k 
                if (k-temp) in dic or (temp==0 and 0 in dic): # 看看互补的东西在不在
                    return True
                else:
                    changeDic = {}
                    for item in dic:
                        changeDic[(item+temp)%k] = 1
                    changeDic[temp] = 1
                    dic = changeDic
            return False
        
s = Solution()
print s.checkSubarraySum([0,0],-1)