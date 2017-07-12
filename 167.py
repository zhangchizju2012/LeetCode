#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:20:34 2017

@author: zhangchi
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, item in enumerate(numbers):
            if (target-item) in dic:
                return [dic[target-item]+1,index+1]
            else:
                dic[item] = index