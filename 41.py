#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:09:08 2017

@author: zhangchi
"""

class Solution(object):
    # 自己写的，没看答案
    # 这题是写完442, 268, 448, 287后写的，与那些题都类似
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        temp = None
        for item in nums:
            if item > 0:
                temp = item
                break
        if temp is None:
            return 1
        for i in xrange(length):
            if nums[i] <= 0:
                nums[i] = temp
        # 上面的处理：出现负数或者0会影响结果，把他们都替换成序列中第一次出现的正数（不能随意赋值，万一刚好赋了缺的值）
        # 会干扰的原因，最后就是判断哪个数还是正的，要是正的对应的index就是结果，如果开始就是0或者负的显然会影响

        for item in nums:
            if item > length: # item过大超过length,要找的数肯定比这个数要小，不用理会这个数
                pass
            else:
                if nums[abs(item)-1] > 0: # 常规解法
                    nums[abs(item)-1] = -nums[abs(item)-1]
        for index,item in enumerate(nums): 
            if item > 0: # 正数对应的就是结果
                return index+1
        return length + 1 # 到这一行，说明前面的数全是正的，且完全有1,2,3...n组成，如[3,4,2,1]
                
s = Solution()
print s.firstMissingPositive([3,4,2,1])