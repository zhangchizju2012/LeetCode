#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:30:53 2017

@author: zhangchi
"""

def find_duplicates_v1(arr1, arr2):
  #pass # your code goes here
  a = 0
  b = 0
  result = []
  while a < len(arr1) and b < len(arr2):
    if arr1[a] < arr2[b]:
      a += 1
    elif arr1[a] > arr2[b]:
      b += 1
    else:
      result.append(arr1[a])
      a += 1
      b += 1
  return result

def find_duplicates(arr1, arr2):
  result = []
  for item in arr2:
    if check(arr1, item) is True:
      result.append(item)
  return result
  
def check(arr, item):
  # it will be used to check whether item in arr or not
  left = 0
  right = len(arr) - 1
  while left <= right:
    middle = (left + right) // 2
    value = arr[middle]
    if value < item:
      left = middle + 1
    elif value > item:
      right = middle - 1
    else:
      return True
  # if we didn't find item
  return False
# it's not good, but i want do it firstly.

# when i check 2, it gets wrong result
# i will use 2 to walk through my code
# left = 0, right = 5 at the beginning
# middle = 2 --> value = 3 > 2
# then right = 2 - 1 = 1, left = 0, middle = 0
# then left = 1, right = 1

# good keep going

# sorry nevermind it isn't consecutive
# ok good idea

arr1 = [1, 2, 3, 5, 6, 7]
for item in arr1:
  print check(arr1, item)
print check(arr1, 4)

# still has bugs.

# yes i see it

# what happens when left == right? tbat was a hint :)

# i think in about 5 min we switch roles, so think about it for another 2 min and then i'll
# show you

# another hint, which case failed?


# lets try to clean this up a little bit.. look for bugs and remove duplication
# yeah, i also think there exists some bugs in my code.
# binary search is used so frequently you should be able to write it very quickly
# i often use it when i interview candidates 
# understood.
# but doing great so far, i just wanted to let you know
  
  
  
  
  # works for me

# ok great. that was simple... can you consider the case where M >> N

# to reduce time complexity, we don't want to walk through arr1, so the idea is maybe i can walk through each element in arr2, then check whether they are in arr1 or not, we can use binary search algo to check because arr1 is sorted. each element will cause O(logM) time complexit, the total complexity will be O(NlogM)... good

# good.. you got it... want to write it? 
# ok

#Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

#Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

