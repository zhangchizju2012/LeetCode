#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 19:38:20 2017

@author: zhangchi
"""

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        equalPos = equation.find("=")
        leftX, leftValue = self.helper(equation[:equalPos])
        rightX, rightValue = self.helper(equation[equalPos+1:])
        xCount = leftX - rightX
        valueCount = leftValue - rightValue
        if xCount == 0:
            if valueCount == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x="+str(-1*valueCount/xCount)
    
    def helper(self, equ):
        # 用来表示有x前面系数是多少，常数是多少
        if equ[0] != '-':
            equ = "+" + equ
        number = ""
        fuhao = ""
        xCount = []
        valueCount = []
        for item in equ:
            if item == "+" or item == "-":
                if fuhao == "":
                    fuhao = item
                else:
                    if fuhao == "+":
                        valueCount.append(int(number))
                    else:
                        valueCount.append(-1*int(number))
                    fuhao = item
                    number = ""
            elif item == "x":
                if number == "":
                    number = "1"
                if fuhao == "+":
                    xCount.append(int(number))
                else:
                    xCount.append(-1*int(number))
                fuhao = ""
                number = ""
            else:
                number += item
        if number != "":
            if fuhao == "+":
                valueCount.append(int(number))
            else:
                valueCount.append(-1*int(number))
        #return xCount, valueCount
        return sum(xCount), sum(valueCount)
                
s = Solution()
#print s.helper("6+x-2")
print s.solveEquation("x=x+2")