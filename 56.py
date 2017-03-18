#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 15:02:59 2017

@author: zhangchi
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
def quickSort(data):
    quickSort_helper(data,0,len(data)-1)
    
def quickSort_helper(data,first,last): 
    if first<last:
        pivot = partition(data,first,last) # partition around a pivot
        quickSort_helper(data,first,pivot-1) 
        quickSort_helper(data,pivot+1,last)

def partition(data,first,last): 
    pivotValue=data[first].start 
    leftMark=first+1 
    rightMark=last
    done = False
    # choosing the pivot as the first element in the list
    # leftMark indicates the end of the first partition (+1)
    # rightMark indicates the beginning of the second partition
    while not done:
        while leftMark<= rightMark and data[leftMark].start <= pivotValue:
            leftMark = leftMark + 1 # shifting the pointer to the right
        while rightMark >= leftMark and data[rightMark].start >= pivotValue: 
            rightMark = rightMark - 1
        if rightMark < leftMark: 
            done = True
        else:
            temp= data[leftMark] 
            data[leftMark] = data[rightMark] 
            data[rightMark]=temp
    temp= data[first]
    data[first] = data[rightMark] 
    data[rightMark]=temp
    return rightMark

def bubbleSortTrackingExchange(data) :
# Sort the given Array with Bubble sort method (Ascending order) # We keep track if exchanges were made and
# stop if no exchanges are made in a given pass
    exchange = True
    last = len(data)-1
    while exchange and last>=0:
        exchange = False
        for current in range (last):
            if ( data[current].start > data[current+1].start ): 
                temp = data[current] 
                data[current]=data[current+1] 
                data[current+1]=temp
                exchange = True 
        last-=1

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        #bubbleSortTrackingExchange(intervals)
        quickSort(intervals)
        result = []
        for i in range(len(intervals)):
            if i == 0:
                lastStart = intervals[i].start
                lastEnd = intervals[i].end
            else:
                if intervals[i].start > lastEnd:
                    result.append(Interval(lastStart,lastEnd))
                    lastStart = intervals[i].start
                    lastEnd = intervals[i].end
                else:
                    lastEnd = max(lastEnd,intervals[i].end)
        result.append(Interval(lastStart,lastEnd))
        return result