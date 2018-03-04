#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:04:24 2018

@author: zhangchi
"""

class Solution(object):
    # dp
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        dic = {}
        num = 10 ** 9 + 7
        dic[1] = 1
        dic[2] = 2
        #dic[3] = 5
        if N in dic:
            return dic[N]
        else:
            for i in range(3,N+1):
                val = 0
                # 相当于分成两部分，i-j和j，j的部分必须是合并在一起的，这样才能避免重复（i-j部分可以不是合并的）
                for j in range(1,i):
                    if j <= 2:
                        # 1或者2的时候只有一种可能性
                        val += dic[i-j]
                    else:
                        val += dic[i-j] * 2
                val += 2
                dic[i] = val % (num)
            return dic[N]
        
s = Solution()
print s.numTilings(4)