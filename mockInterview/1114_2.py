#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:31:57 2017

@author: zhangchi
"""

#def index_equals_value_search_origin(arr):
  #pass # your code goes here
#  for index, item in enumerate(arr):
#    if index == item:
#      return index
#  return -1

def index_equals_value_search(arr):
  return index_equals_value_search_(arr,0)

def index_equals_value_search_(arr, index):
  length = len(arr)
  if length == 0:
    return -1
  elif length == 1:
    if arr[0] == index:
      return 0
    else:
      return -1
  middle = length // 2
  middleValue = arr[middle]
  if middleValue > middle + index:
    return index_equals_value_search_(arr[:middle],index)
  elif middleValue == middle + index:
    result = index_equals_value_search_(arr[:middle],index)
    if result == -1:
      return middle
    else:
      return result
  else:
    result = index_equals_value_search_(arr[middle+1:],index+middle+1)
    if result == -1:
      return -1
    else:
      return middle + 1 + result
print index_equals_value_search([-6,-5,-4,-1,1,3,5,7])
    
# [-8,0,1,3,5] middleValue = 1, middle = 2
# [3,5] middleValue = 5, middle = 1

# [-8,2,4,7,8,12,15,17] -> -1
# [0,2,4,7,8,12,15,17] -> 0
# [-5,-2,-1,0,1]