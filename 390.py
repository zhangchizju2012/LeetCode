#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:05:53 2017

@author: zhangchi
"""

class Solution(object):
    # inspired by https://discuss.leetcode.com/topic/59293/java-easiest-solution-o-logn-with-explanation
    # 看了这个解释的前三行写的code，没完整看
    # 不断更新head指针和step，知道只剩一个元素，head指针指向的元素就是最后剩下的元素
    # 只有向右移动或者向左移动且n是奇数时候，head指针才会移动（只有这两种情况，序列的第一个数才会被挪掉）
    # 每次移动，step都会增加一倍，因为有一半的元素被挪走了
    # 可以画一画19，21的图，就有感觉了
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        step = 1
        direction = 'l'
        while n != 1:
            if direction == 'l' or n % 2 == 1:
                start += step
                n = n // 2
                step *= 2
            else:
                step *= 2
                n = n // 2
            if direction == 'l':
                direction = 'r'
            else:
                direction = 'l'
        return start
        
s = Solution()
print s.lastRemaining(11111111)