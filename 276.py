#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:47:57 2017

@author: zhangchi
"""

class Solution(object):
    # 通项公式： A_n = (k-1)A_(n-1) + (k-1)A_(n-2)
    # 假设第一个数和第二个数不同，则可能性有(k-1)A_(n-1)
    # 假设第一个数和第二个数相同，则可能性有(k-1)A_(n-2)
    # 自己想的
    # 拓展：如果这个fence是一个环，怎么办？
    # 另外的拓展，假设任意两个相邻的颜色都不能相同，然后是一个环
    # 那么通项公式为：A_n = (k-2)A_(n-1) + (k-1)A_(n-2)
    # 原因：假设第一个和最后第二个相同，则最后一个能在（n-1）里选择，第一个和最后第二个相同可以看成A_(n-2)
    # 原因：假设第一个和最后第二个不同，则最后一个能在（n-2）里选择，第一个和最后第二个不同可以看成A_(n-1)
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        elif n == 2:
            return k ** 2
        else:
            a = [k,k**2]
            for _ in xrange(n-2):
                a.append((a[-1]*(k-1)+a[-2]*(k-1)))
            return a[-1]
        
    