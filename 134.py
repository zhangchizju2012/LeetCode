#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 19:57:49 2017

@author: zhangchi
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0:
            return 0
        dif = []
        for a,b in zip(gas,cost):
            dif.append(a-b)
        for i in range(len(dif)):
            if dif[i] >= 0:
                temp = 0
                label = True
                for item in dif[i:] + dif[:i]:
                    temp += item
                    if temp < 0:
                        label = False
                        break
                if label == True:
                    return i
        return -1