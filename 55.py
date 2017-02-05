#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:18:16 2017

@author: zhangchi
"""

class Solution(object):
    def __init__(self):
        self.dict = []
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        
        if length in self.dict:
            return False     
            
        if length == 0 or length == 1:
            return True
        for i in range(nums[0],0,-1):
            if i == nums[0] and i+1 >= length:
                return True
            else:
                if self.canJump(nums[i:]) == False:
                    pass
                else:
                    return True
        self.dict.append(length)
        return False
            
S = Solution()
nums = [2,3,1,1,4]
print S.canJump(nums)

#bool canJump(int A[], int n) {#n代表长度，可以再进化，i < n && i <= reach &&  reach <= n
#    int i = 0;
#    for (int reach = 0; i < n && i <= reach; ++i)
#        reach = max(i + A[i], reach);
#    return i == n;
#}
#关键：一格一格走过去（看最远能走的距离能否cover序列末端），我的：先往最远的走，不行再用近的

'''
class Solution {
public:
  bool canJump(int A[], int n) {
    int i = 0, maxreach = 0;
    for (; i < n && i <= maxreach && maxreach < n - 1; ++i)
      maxreach = max(maxreach,i+A[i]);
    return maxreach>=n-1;
  }
};
'''
