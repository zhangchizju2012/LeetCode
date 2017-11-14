#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:41:44 2017

@author: zhangchi
"""

def flip(arr, k):
  arr[:k] = arr[:k][::-1]
  return arr

  
def pancake_sort(arr):

  # first put largest at end
  # and then find largest in rest of array put it in n-1 index
  
  # repeat
  #largest can be found by arr.index(max(arr))
  #pass # your code goes here
  if len(arr) == 0:
    return arr
  length = len(arr)
  l = length
  while l > 0 :
    largest = arr[0]
    largest_index = 0
    for index, item in enumerate(arr[:l]):
      if item > largest:
        largest = item
        largest_index = index
    if largest < l + 1:
      arr = flip(arr, largest_index+1)
      arr = flip(arr, l)
      l -= 1
  return arr

# [1,5,4,3,2] l = 5, largest_index = 1, [5,1,4,3,2] [2,3,4,1,5]
# [2,3,4,1,5] l = 4, largest_index = 2, [4,3,2,1,5], [1,2,3,4,5]
# [1,2,3,4,5] l = 3, largest_index = 2
    


# arr = [1,5,4,3,2] - > [1,2,3,4,5]
# [1,5,4,3,2] - > [2,3,4,5,1] -> [5,4,3,2,1] - > [1,2,3,4,5]

# [5,1,4,3,2] -> [2,3,4,1,5] 1 element is sorted. Need to worry about rest
# [4,3,2,1,5] - > [1,2,3,4,5]

# flip(arr,5)