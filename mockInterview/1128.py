#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:23:49 2017

@author: zhangchi
"""

# slotsA = [[10, 50], [60, 120], [140, 210]]
# slotsB = [[0, 15], [60, 70]]
# dur = 8
# [10,15] -> 5 < 8
# [60,70] -> 10 > 8 
# return [60,60+8]

# slotsA = [[10, 50], [60, 120], [140, 210]]
# slotsB = [[0, 15], [60, 70]]
# [10,15] -> 5 < 12
# [60,70] -> 10 < 12
# return null

# ok.

def meeting_planner(slotsA, slotsB, dur):
  # pass # your code goes here
  # i'm thinking.
  # i'm thinking about how to calculate the intersect in code.
  lengthA = len(slotsA)
  lengthB = len(slotsB)
  #intersectList = []
  indexA = 0
  indexB = 0
  # to get intersect, i need walk through both slotsA and slotsB
  while indexA < lengthA and indexB < lengthB:
    # when slotsA[index] and slotsB[index] has intersect.
    if max(slotsA[indexA][0], slotsB[indexB][0]) < min(slotsA[indexA][1], slotsB[indexB][1]):
      # check whether the intersect is enough
      if min(slotsA[indexA][1], slotsB[indexB][1]) - max(slotsA[indexA][0], slotsB[indexB][0]) >= dur:
        return [max(slotsA[indexA][0], slotsB[indexB][0]),max(slotsA[indexA][0], slotsB[indexB][0])+dur]
    if slotsA[indexA][1] > slotsB[indexB][1]:
      indexB += 1
    else:
      indexA += 1
  return []
    
    
slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
print meeting_planner(slotsA, slotsB, dur)