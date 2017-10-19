#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 14:17:28 2017

@author: zhangchi
"""
def bubbleSortTrackingExchange(data) :
# Sort the given Array with Bubble sort method (Ascending order) # We keep track if exchanges were made and
# stop if no exchanges are made in a given pass
    exchange = True
    last = len(data)-1
    while exchange and last>=0:
        exchange = False
        for current in range (last):
            if ( data[current] > data[current+1] ): 
                temp = data[current] 
                data[current]=data[current+1] 
                data[current+1]=temp
                exchange = True 
        last-=1

def quickSort(data):
# Sort myself using a quick sort. 
    quickSort_helper(data,0,len(data)-1)
def quickSort_helper(data,first,last): 
    if first<last:
        pivot = partition(data,first,last) # partition around a pivot
        quickSort_helper(data,first,pivot-1) 
        quickSort_helper(data,pivot+1,last)
        #sort 1st half # sort 2nd half
def partition(data,first,last): 
    pivotValue=data[first] 
    leftMark=first+1 
    rightMark=last
    done = False
    # choosing the pivot as the first element in the list
    # leftMark indicates the end of the first partition (+1)
    # rightMark indicates the beginning of the second partition
    while not done:
        while leftMark<= rightMark and data[leftMark] <= pivotValue:
            leftMark = leftMark + 1 # shifting the pointer to the right
        while rightMark >= leftMark and data[rightMark] >= pivotValue: 
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

data = [1,0]
bubbleSortTrackingExchange(data)