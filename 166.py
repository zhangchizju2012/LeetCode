#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:28:09 2017

@author: zhangchi
"""

class Solution(object):
    # 看了tag, hash function，其他都没看，自己写的
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0: # 分母为0没有意义
            return "NaN"
        if numerator * denominator < 0: # 分子分母有一个是负数的话先结果加上符号，然后当正数处理
            result = "-"
        else:
            result = ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        result += str(numerator//denominator) # 正数部分处理
        if numerator % denominator == 0:
            return result
        else:
            result += "."
            length = len(result)
            dic = {} # 记录分母部分出现过的情况，如果再次出现，说明是无限循环小数
            numerator = (numerator % denominator) * 10
            while True:
                if numerator == 0:
                    return result
                elif numerator not in dic:
                    dic[numerator] = length # 记录了result新加的数所出现的位置，用于之后加左括号(
                    result += str(numerator//denominator)
                    length += 1
                    numerator = (numerator%denominator)*10
                else:
                    index = dic[numerator]
                    print index
                    result = result[:index] + "(" + result[index:] + ")"
                    return result
                    
s = Solution()
print s.fractionToDecimal(-13,24)
        