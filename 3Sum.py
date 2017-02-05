#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:39:23 2016

@author: zhangchi
"""

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    '''
    if len(nums) < 3:
        return []
    result = set()
    nums.sort()
    for i in range(len(nums)):
        target = -nums[i]
        pointA = 0
        pointB = len(nums)-1
        if pointA == i:
            pointA = pointA + 1
        if pointB == i:
            pointB = pointB - 1
        while nums[pointA] + nums[pointB] != target:
            if pointA == pointB:
                break
            if pointA == i:
                pointA = pointA + 1
            if pointB == i:
                pointB = pointB - 1
            if nums[pointA] + nums[pointB] < target:
                pointA = pointA + 1
            else:
                pointB = pointB - 1
        if pointA != pointB and nums[pointA] + nums[pointB] == target:
            if i < pointA:
                result.add((nums[i],nums[pointA],nums[pointB]))
            if i > pointA and i < pointB:
                result.add((nums[pointA],nums[i],nums[pointB]))
            if i > pointB:
                result.add((nums[pointA],nums[pointB],nums[i]))
    final = []
    for _ in range(len(result)):
        temp = []
        tempset = result.pop()
        for i in range(3):
            temp.append(tempset[i])
        final.append(temp)
    return final
    '''
    nums.sort()
    res = []
    length = len(nums)
    for i in range(0, length - 2):
        if i and nums[i] == nums[i - 1]:
            continue
        target = nums[i] * -1
        left, right = i + 1, length - 1
        while left < right:
            if nums[left] + nums[right] == target:
                res.append([nums[i], nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
    return res
    
print threeSum([-1, 0, 1, 2, -1, -4,-2,4,5,6,-4,-5,-6])