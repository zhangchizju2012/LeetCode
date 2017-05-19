#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:15:55 2017

@author: zhangchi
"""

class Solution(object):
    # DP问题
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            if nums[0] >= 0:
                return True
            else:
                return False
        self.dic = {}
        # self.dic里存储的是index从i到j的nums，第一个抓数的人所抓的值最高比第二个人多多少（可正可负，负说明第二个的值更高）
        self.nums = nums
        length = len(nums)
        value = self.helper(0,length-1)
        if value < 0:
            return False
        else:
            return True
        
    def helper(self,i,j):
        if (i,j) not in self.dic:
            if j - i == 1:
                temp = max(self.nums[i]-self.nums[j],self.nums[j]-self.nums[i])
            else:
                # 注意这里是减，考虑self.dic的意义（line22），就明白了
                temp = max(self.nums[i]-self.helper(i+1,j),self.nums[j]-self.helper(i,j-1))
            self.dic[(i,j)] = temp
        return self.dic[(i,j)]
                        
s = Solution()
print s.PredictTheWinner([1,1])