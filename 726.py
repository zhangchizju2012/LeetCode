#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 20:44:11 2017

@author: zhangchi
"""

class Solution(object):
    # 主要就是预处理比较烦
    def preprocess(self, formula):
        result = []
        length = len(formula)
        i = 0
        variable = ""
        #count = ""
        while i < length:
            if (formula[i] == "(") or (formula[i] == ")"):
                if len(variable) > 0:
                    if variable.isdigit() == False:
                        result.append(variable)
                        result.append(1)
                    else:
                        result.append(int(variable))
                    variable = ""
                result.append(formula[i])
                if (i+1) < length and formula[i+1].isdigit():
                    pass
                else:
                    result.append(1)
            elif "A" <= formula[i] <= "Z":
                if len(variable) > 0:
                    if variable.isdigit() == False:
                        result.append(variable)
                        result.append(1)
                    else:
                        result.append(int(variable))
                    variable = ""
                variable += formula[i]
            elif "a" <= formula[i] <= "z":
                variable += formula[i]
            elif formula[i].isdigit():
                if len(variable) > 0 and variable.isdigit() == False:
                    result.append(variable)
                    variable = ""
                variable += formula[i]
            i += 1
        if len(variable) > 0:
            if variable.isdigit() == False:
                result.append(variable)
                result.append(1)
            else:
                result.append(int(variable))
        return result
# =============================================================================
#     def preprocess(self, formula):
#         result = []
#         length = len(formula)
#         i = 0
#         variable = ""
#         #count = ""
#         while i < length:
#             if (formula[i] == "(") or (formula[i] == ")"):
#                 if len(variable) > 0:
#                     result.append(variable)
#                     variable = ""
#                 result.append(formula[i])
#             elif "A" <= formula[i] <= "Z":
#                 if len(variable) > 0:
#                     result.append(variable)
#                     variable = ""
#                 variable += formula[i]
#             elif "a" <= formula[i] <= "z":
#                 variable += formula[i]
#             elif formula[i].isdigit():
#                 if len(variable) > 0 and variable.isdigit() == False:
#                     result.append(variable)
#                     variable = ""
#                 variable += formula[i]
#             i += 1
#         if len(variable) > 0:
#             result.append(variable)
#         return result
# =============================================================================
        
    # 用stack就能解决，碰到），把上一次（之后的东西全都拿出来，乘上需要的倍数，然后再放回去
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        temp = self.preprocess(formula)
        stack = []
        i = 0
        length = len(temp)
        while i < length:
            if temp[i] == "(":
                stack.append("(")
                i += 2
            elif temp[i] == ")":
                size = temp[i+1]
                now = []
                pop = stack.pop()
                while pop != "(":
                    now.append([pop[0],pop[1]*size])
                    pop = stack.pop()
                stack += now
                i += 2
            else:
                stack.append([temp[i],temp[i+1]])
                i += 2
                
        dic = {}
        for item in stack:
            if item[0] in dic:
                dic[item[0]] += item[1]
            else:
                dic[item[0]] = item[1]
                
        key = dic.keys()
        key.sort()
        
        result = ""
        for item in key:
            result += item
            if dic[item] > 1:
                result += str(dic[item])
        return result
                

        
s = Solution()
print s.countOfAtoms("H2O")