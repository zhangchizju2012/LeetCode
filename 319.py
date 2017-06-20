#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:23:41 2017

@author: zhangchi
"""

class Solution(object):
    # 解释：https://discuss.leetcode.com/topic/31929/math-solution
    # 关键，除了平方数，其他数的因子都是成对出现的，最后都会导致灯泡灭掉，所以只要统计平方数的个数就好了
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n))