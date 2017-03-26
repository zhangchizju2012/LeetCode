#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 18:56:15 2017

@author: zhangchi
"""
import copy

class solution():
    def __init__(self):
        self.result = []
        
    def hammingDistance(self,listNumber,count,stopPosition=[]):
        if count == 0:
            if listNumber not in self.result:
                self.result.append(listNumber)
        else:
            count = count - 1
            for i in range(len(listNumber)):
                if i not in stopPosition:
                    templistNumber = listNumber[:i] + [1^listNumber[i]] + listNumber[i+1:]
                    tempStopPosition = copy.deepcopy(stopPosition)
                    tempStopPosition.append(i)
                    self.hammingDistance(templistNumber,count,tempStopPosition)
        '''
        if count == 1:
            for i in range(len(listNumber)):
                if i not in stopPosition:
                    tempResult = listNumber[:i] + [1^listNumber[i]] + listNumber[i+1:]
                    if tempResult not in self.result:
                        self.result.append(tempResult)
        else:
            count = count - 1
            for i in range(len(listNumber)):
                if i not in stopPosition:
                    templistNumber = listNumber[:i] + [1^listNumber[i]] + listNumber[i+1:]
                    tempStopPosition = copy.deepcopy(stopPosition)
                    tempStopPosition.append(i)
                    self.hammingDistance(templistNumber,count,tempStopPosition)
        '''
                    
S = solution()
listNumber = [0,0,0,0,0,1,1,1,0,0]
count = 4
S.hammingDistance(listNumber,count)
print S.result
print len(S.result)

def humming(s,k):
    if k==0:return [s]
    else:
        output=[]
        for i in range(len(s)):
            lists=humming(s[i+1:],k-1)
            if lists is not None:
                for item in lists:
                    output.append(s[:i]+str(1^int(s[i]))+item)
        return output
    
