#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 20:05:40 2017

@author: zhangchi
"""

class Solution(object):
    def gcd(self,a,b):
        if a % b == 0:
            return b
        else:
            return self.gcd(b,a % b)
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        plusOrMinus = []
        if expression[0] == '-':
            plusOrMinus.append('-')
            expression = expression[1:]
        else:
            plusOrMinus.append('+')
        value = []
        while len(expression) > 0:
            positionP = expression.find('+')
            positionM = expression.find('-')
            if positionP == -1 and positionM == -1:
                value.append(expression)
                expression = ''
            elif positionP == -1:
                plusOrMinus.append('-')
                value.append(expression[:positionM])
                expression = expression[positionM+1:]
            elif positionM == -1:
                plusOrMinus.append('+')
                value.append(expression[:positionP])
                expression = expression[positionP+1:]
            elif positionM < positionP:
                plusOrMinus.append('-')
                value.append(expression[:positionM])
                expression = expression[positionM+1:]
            elif positionM > positionP:
                plusOrMinus.append('+')
                value.append(expression[:positionP])
                expression = expression[positionP+1:]
        numerator = 0
        denominator = 1
        for a,b in zip(plusOrMinus,value):
            position = b.find('/')
            nu = int(b[:position])
            de = int(b[position+1:])
            if a == '+':
                numerator = numerator * de + nu * denominator
            else:
                numerator = numerator * de - nu * denominator
            denominator = denominator * de
            gcd = self.gcd(numerator,denominator)
            numerator /= gcd
            denominator /= gcd
        return str(numerator)+'/'+str(denominator)

#==============================================================================
# class Solution(object):
#     def fractionAddition(self, expression):
#         """
#         :type expression: str
#         :rtype: str
#         """
#         plusOrMinus = []
#         if expression[0] == '-':
#             plusOrMinus.append('-')
#             expression = expression[1:]
#         else:
#             plusOrMinus.append('+')
#         value = []
#         while len(expression) > 0:
#             positionP = expression.find('+')
#             positionM = expression.find('-')
#             if positionP == -1 and positionM == -1:
#                 value.append(expression)
#                 expression = ''
#             elif positionP == -1:
#                 plusOrMinus.append('-')
#                 value.append(expression[:positionM])
#                 expression = expression[positionM+1:]
#             elif positionM == -1:
#                 plusOrMinus.append('+')
#                 value.append(expression[:positionP])
#                 expression = expression[positionP+1:]
#             elif positionM < positionP:
#                 plusOrMinus.append('-')
#                 value.append(expression[:positionM])
#                 expression = expression[positionM+1:]
#             elif positionM > positionP:
#                 plusOrMinus.append('+')
#                 value.append(expression[:positionP])
#                 expression = expression[positionP+1:]
#         result = 0
#         from fractions import Fraction
#         for a,b in zip(plusOrMinus,value):
#             if a == '+':
#                 result += Fraction(b)
#             else:
#                 result -= Fraction(b)
#         return result
#==============================================================================

#==============================================================================
# class Solution(object):
#     def fractionAddition(self, expression):
#         """
#         :type expression: str
#         :rtype: str
#         """
#         plusOrMinus = []
#         if expression[0] == '-':
#             plusOrMinus.append('-')
#             expression = expression[1:]
#         else:
#             plusOrMinus.append('+')
#         value = []
#         while len(expression) > 0:
#             positionP = expression.find('+')
#             positionM = expression.find('-')
#             if positionP == -1 and positionM == -1:
#                 value.append(expression)
#                 expression = ''
#             elif positionP == -1:
#                 plusOrMinus.append('-')
#                 value.append(expression[:positionM])
#                 expression = expression[positionM+1:]
#             elif positionM == -1:
#                 plusOrMinus.append('+')
#                 value.append(expression[:positionP])
#                 expression = expression[positionP+1:]
#             elif positionM < positionP:
#                 plusOrMinus.append('-')
#                 value.append(expression[:positionM])
#                 expression = expression[positionM+1:]
#             elif positionM > positionP:
#                 plusOrMinus.append('+')
#                 value.append(expression[:positionP])
#                 expression = expression[positionP+1:]
#         result = 0
#         for a,b in zip(plusOrMinus,value):
#             position = b.find('/')
#             v = float(b[:position])/float(b[position+1:])
#             if a == '+':
#                 result += v
#             else:
#                 result -= v
#         from fractions import Fraction
#         if int(result) == result:
#             return str(int(result))+'/1'
#         temp = ''
#         if result < 0:
#             temp = '-'
#             result = -result
#         r = Fraction(result)
#         return temp+str(r.numerator)+'/'+str(r.denominator)
#==============================================================================
            
s = Solution()
print s.fractionAddition("-1/2+1/2")