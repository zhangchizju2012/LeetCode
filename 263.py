#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:36:37 2017

@author: zhangchi
"""

class Solution(object):
    # 按照定义来就好了
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        label = True
        while label:
            label = False
            if num % 2 == 0:
                num = num // 2
                label = True
            if num % 3 == 0:
                num = num // 3
                label = True
            if num % 5 == 0:
                num = num // 5
                label = True
            if label == False:
                if num == 1:
                    return True
                else:
                    return False
        
s = Solution()
print s.isUgly(131072)