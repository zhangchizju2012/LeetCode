#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 23:58:17 2017

@author: zhangchi
"""

def find_pairs_with_given_difference(arr, k):
  #pass # your code goes here
  check = set()
  output = []
  for item in arr:
    if item + k in check:
      output.append([item+k,item])
    if item - k in check:
      output.append([item-k,item])
    check.add(item)
  return output

arr = [0, -1, -2, 2, 1]
k = 1
print find_pairs_with_given_difference(arr, k)