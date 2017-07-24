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
        #stringList = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        # z, ,w, ,u,f,x,v,g,i
        resultDic = {}
        for item in s:
            if item in resultDic:
                resultDic[item] += 1
            else:
                resultDic[item] = 1
        result = []
        if "z" in resultDic:
            result += [0] * resultDic["z"]
        if "w" in resultDic:
            result += [2] * resultDic["w"]
        if "u" in resultDic and resultDic["u"]>0:
            result += [4] * resultDic["u"]
            resultDic["f"] -= resultDic["u"]
        if "f" in resultDic and resultDic["f"]>0:
            result += [5] * resultDic["f"]
            resultDic["v"] -= resultDic["f"]
            resultDic["i"] -= resultDic["f"]
        if "x" in resultDic and resultDic["x"]>0:
            result += [6] * resultDic["x"]
            resultDic["i"] -= resultDic["x"]
        if "v" in resultDic and resultDic["v"]>0:
            result += [7] * resultDic["v"]
            resultDic["n"] -= resultDic["v"]
        if "g" in resultDic and resultDic["g"]>0:
            result += [8] * resultDic["g"]
            resultDic["i"] -= resultDic["g"]
            resultDic["h"] -= resultDic["g"]
        if "i" in resultDic and resultDic["i"]>0:
            result += [9] * resultDic["i"]
            resultDic["n"] -= 2 * resultDic["i"]
        if "n" in resultDic:
            result += [1] * resultDic["n"]
        if "h" in resultDic:
            result += [3] * resultDic["h"]
        result.sort()
        return "".join([str(item) for item in result])
        
s = Solution()
print s.originalDigits("fviefuro")
#==============================================================================
#         dic = {}
#         for index, item in stringList:
#             dic[index] = {}
#             for i in item:
#                 if i not in dic[index]:
#                     dic[index][i] = 1
#                 else:
#                     dic[index][i] += 1
#         for item in s:
#             for i in xrange(10):
#                 if item in dic[i]:
#                     dic[i][item] -= 1
#                     if dic[i][item] == 0:
#                         dic[i].pop(item)
#==============================================================================
