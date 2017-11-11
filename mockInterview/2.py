#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 23:21:05 2017

@author: zhangchi
"""

# =============================================================================
# Getting a Different Number
# 
# Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.
# 
# Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.
# 
# Your algorithm should be efficient, both from a time and a space complexity perspectives.
# 
# Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.
# 
# Analyze the time and space complexities of your algorithm.
# 
# Example:
# 
# input:  arr = [0, 1, 2, 3]
# 
# output: 4 
# Constraints:
# 
# [time limit] 5000ms
# 
# [input] array.integer arr
# 
# 1 ≤ arr.length ≤ MAX_INT
# 0 ≤ arr[i] ≤ MAX_INT for every i, 0 ≤ i < MAX_INT
# [output] integer
# =============================================================================

# O(1) space
def get_different_number(arr):
  length = len(arr)
  for i in xrange(length):
    value = arr[i]
    if value < length:
      arr[i], arr[value] = arr[value], arr[i]
  for i in xrange(length):
    if i != arr[i]:
      return i
  return length

# O(n) space
def get_different_number2(arr):
  dic = set()
  for item in arr:
    dic.add(item)
    
  start = 0
  while True:
    if start in dic:
      start += 1
    else:
      return start
    
  # this is very naive idea, I think maybe i can't pass all tests.
  # maybe i can try firstly.