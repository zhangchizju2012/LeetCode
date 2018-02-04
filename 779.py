#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:50:13 2018

@author: zhangchi
"""

# 观察发现，每个row，都是先重复上一个row，再对上一个row的每一位取反

class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        K = K - 1
        up = N
        result = [0,1,1,0]
        label = True
        while True:
            if K <= 3:
                if label:
                    return result[K]
                else:
                    if result[K] == 1:
                        return 0
                    else:
                        return 1
            for i in range(up, 1, -1):
                if K // (2**i)== 1:
                    K = K % (2**i)
                    label = not label
                    break
                
s = Solution()
for i in range(1,17):
    print s.kthGrammar(5,i)
