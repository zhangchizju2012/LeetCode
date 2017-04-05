#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 23:13:09 2017

@author: zhangchi
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dictionary1 = {}
        dictionary2 = {}
        string = str.split(' ')
        if len(pattern) != len(string):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dictionary1:
                dictionary1[pattern[i]] = string[i]
            else:
                if dictionary1[pattern[i]] != string[i]:
                    return False
            if string[i] not in dictionary2:
                dictionary2[string[i]] = pattern[i]
            else:
                if dictionary2[string[i]] != pattern[i]:
                    return False
        return True