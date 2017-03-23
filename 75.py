#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:11:18 2017

@author: zhangchi
"""

def quickSort(dataSet):
    quickSortHelp(dataSet,0,len(dataSet)-1)
    return dataSet

def partition(data,first,last): 
    pivotValue=data[first] 
    leftMark=first+1 
    rightMark=last
    while rightMark >= leftMark:
        while leftMark<= rightMark and data[leftMark] <= pivotValue:
            leftMark = leftMark + 1 # shifting the pointer to the right
        while rightMark >= leftMark and data[rightMark] >= pivotValue: 
            rightMark = rightMark - 1
        if rightMark >= leftMark: 
            data[leftMark], data[rightMark] = data[rightMark], data[leftMark]
    data[first], data[rightMark] = data[rightMark], data[first]
    return rightMark
    
def quickSortHelp(dataSet,start,end):
    if start < end:
        middel = partition(dataSet,start,end)
        quickSortHelp(dataSet,start,middel-1)
        quickSortHelp(dataSet,middel+1,end)
        
def main():    
    a = [1,2]
    print quickSort(a)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        quickSort(nums)
'''    
# work    
def partition(data,first,last): 
    leftMark=first+1 
    rightMark=last
    while rightMark >= leftMark:
        
        for i in range(leftMark,rightMark+1):
            if data[i] <= data[first]:
                leftMark = leftMark + 1
            else:
                break
        
        #while leftMark<= rightMark and data[leftMark] <= data[first]:
        #    leftMark = leftMark + 1 # shifting the pointer to the right
        while rightMark >= leftMark and data[rightMark] >= data[first]: 
            rightMark = rightMark - 1
        if rightMark >= leftMark: 
            data[leftMark], data[rightMark] = data[rightMark], data[leftMark]
    data[first], data[rightMark] = data[rightMark], data[first]
    return rightMark    
    

# doesn't work
def partition(dataSet,start,end):
    left = start+1
    right = end
    while left < right:
        for i in range(left,right+1):#wrong 
            if dataSet[i] > dataSet[start] or i == right:
                left = i
                break
        for i in range(right,left-1,-1):
            if dataSet[i] < dataSet[start] or i == left:
                right = i
                break
        if left < right:
            dataSet[left], dataSet[right] = dataSet[right], dataSet[left]
        else:
            break
    dataSet[start], dataSet[right] = dataSet[right], dataSet[start]
    return right
# doesn't work
def partition(dataSet,start,end):
    left = start
    right = end
    lastLeft = None
    lastRight = None
    while left < right:
        lastLeft = left
        lastRight = right
        for i in range(left+1,end):
            if dataSet[i] > dataSet[start]:
                left = i
                break
        for i in range(right,start,-1):
            if dataSet[i] < dataSet[start]:
                right = i
                break
        if left < right:
            dataSet[left], dataSet[right] = dataSet[right], dataSet[left]
    dataSet[start], dataSet[lastLeft] = dataSet[lastLeft], dataSet[start]
    return lastLeft
'''
    