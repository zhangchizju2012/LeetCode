#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:16:20 2017

@author: zhangchi
"""

def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        result = strs[0]
        for item in strs:
            temp = ""
            for i in range(min(len(result),len(item))):
                if result[i] == item[i]:
                    temp += result[i]
                else:
                    break
            if temp == "":
                result = ""
                break
            else:
                result = temp
        return result