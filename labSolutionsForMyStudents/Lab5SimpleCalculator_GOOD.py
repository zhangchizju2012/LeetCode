#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:07:08 2017

@author: zhangchi
"""
'''
3 + 4 * 2 / ( 5 -1 ) + ( 2 + 3 )
--->
3 4 2 * 5 1 -/ 2 3 + + +
--->
10
'''

# inputString = "3+4*2/(5-1)+(2+3)"
# inputString = "((1+2)*3-(4-5)*(6+7))"
inputString = "1+2+3+4*5"
output = []
operator = []
dictionary = {'+':1,'-':1,'*':2,'/':2}
for item in inputString:
    if item in "1234567890":
        output.append(item)
    else:
        if len(operator) == 0 or item == '(' or operator[-1] == '(':
            operator.append(item)
        elif item == ')':
            while operator[-1] != '(':
                output.append(operator.pop())
            operator.pop()
        else:
            if dictionary[operator[-1]] < dictionary[item]:
                operator.append(item)
            else:
                output.append(operator.pop())
                operator.append(item)
while len(operator)>0:
    output.append(operator.pop())

result = []    
for item in output:
    if item in "0123456789":
        result.append(item)
    else:
        temp2 = result.pop()
        temp1 = result.pop()
        if item == "*":
            temp3 = float(temp1) * float(temp2)
        elif item == '/':
            temp3 = float(temp1) / float(temp2)
        elif item == '+':
            temp3 = float(temp1) + float(temp2)
        else:
            temp3 = float(temp1) - float(temp2)
        result.append(temp3)