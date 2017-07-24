#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 23:02:41 2017

@author: zhangchi
"""

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stringList = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        dic = {}
        for index, item in stringList:
            dic[index] = {}
            for i in item:
                if i not in dic[index]:
                    dic[index][i] = 1
                else:
                    dic[index][i] += 1
        for item in s:
            for i in xrange(10):
                if item in dic[i]:
                    dic[i][item] -= 1
                    if dic[i][item] == 0:
                        dic[i].pop(item)