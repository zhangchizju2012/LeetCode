#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:51:23 2016

@author: zhangchi
"""
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    heightlength = len(height)
    left = 0
    right = heightlength - 1
    size = getSize(left,right,height)
    while left < right:
        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1
        tempsize = getSize(left,right,height)
        size = max(size,tempsize)
    return size

def getSize(left,right,height):
    return min(height[left],height[right])*abs(right-left)
    
print maxArea([1,4,5,6,6,7,7,8,8,9,9,0,0,5,4,3,7])
'''
def get(direction,position,height):
    for i in range(len(height)):
        if direction == 'left':
            if height[i] >= height[position]:
                return (position-i)*height[position], i
        if direction == 'right':
            if height[len(height)-1-i] >= height[position]:
                return (len(height)-1-i-position)*height[position], len(height)-1-i
    return 0, -1
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
'''
'''
    heightlength = len(height)
    left = 0
    right = heightlength - 1
    size = getSize(left,right,height)
    while left < right:
        sizeLeft, indexLeft = get('left',right,height)
        sizeRight, indexRight = get('right',left,height)
        if max(sizeLeft,sizeRight) > size:
            if sizeLeft ==max(sizeLeft,sizeRight):
                size = sizeLeft
                left = indexLeft
            else:
                size = sizeRight
                right = indexRight
        elif max(sizeLeft,sizeRight) == size:
            if sizeLeft == size:
                left = left + 1
            else:
                right = right -1
        else:
            left = left + 1
            right = right -1
    return size
'''
'''
    heightlength = len(height)
    left = 0
    right = heightlength - 1
    size = getSize(left,right,height)
    while left < right:
        sizeLeft, indexLeft = get('left',right,height)
        sizeRight, indexRight = get('right',left,height)
        if max(sizeLeft,sizeRight) > size:
            size = max(sizeLeft,sizeRight)
        if sizeLeft ==max(sizeLeft,sizeRight):
            left = max(indexLeft,left)
            right = right - 1
        else:
            right = min(indexRight,right)
            left = left + 1
    return size
'''
'''
print maxArea([1,2,4,3])
'''