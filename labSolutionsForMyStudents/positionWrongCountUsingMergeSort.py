#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:53:25 2017

@author: zhangchi
"""

class Solution:
    def __init__(self):
        self.number = 0
    def merge(self,left,right): 
        result=[]
        i,j=0,0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]: 
                result.append(left[i]) 
                i+=1
            else: 
                result.append(right[j]) 
                j+=1
                self.number+=len(left)
        result += left[i:] 
        result += right[j:]
        return result
    
    def mergeSort(self,data):
    # Sort myself using a merge sort.
        if len(data) <=1: 
            return data
        middle = len(data)//2
        left=self.mergeSort(data[:middle])
        right=self.mergeSort(data[middle:])
        return self.merge(left,right)

s = Solution()
print s.mergeSort([10,9,8,7,6,5,4,3,2,1])
print s.number
