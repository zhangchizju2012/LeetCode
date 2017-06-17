#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 12:30:42 2017

@author: zhangchi
"""

class Solution(object):
    # dfs，感觉之前做过类似的
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.target = n
        self.result = []
        self.helper([0],0,k)#[0]是为了配合后面line27
        return self.result

    def helper(self,previous,now,k):
        if now == self.target:
            if k == 0:
                self.result.append(previous[1:])
        else:
            for i in xrange(previous[-1]+1,10):#previous[-1]开始算，前面已经考虑过了
                if self.target - now >= i:
                    self.helper(previous+[i],now+i,k-1)
                else:
                    break
                
s = Solution()
print s.combinationSum3(1,1)
            