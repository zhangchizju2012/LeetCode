#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 20:20:49 2017

@author: zhangchi
"""

class Solution(object):
    # 自己写的，比赛题
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dic = {}
        for i in xrange(1,7):
            # 前面几个可以轻松找到答案
            # 之后不可能再直接输入A
            dic[i] = i
        if N in dic:
            return dic[N]
        else:
            for i in xrange(7,N+1):
                value = -float('inf')
                for j in xrange(3,7):
                    value = max(value,(j-1)*dic[i-j])
                    # j-1的来源：多3个，最多翻2倍；多4个，最多翻3倍；多5个，最多翻4倍；多6个，最多翻5倍；
                dic[i] = value
            return dic[N]

s = Solution()
print s.maxA(50)