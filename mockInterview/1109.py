#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 22:53:35 2017

@author: zhangchi
"""

# =============================================================================
# Sentence Reverse
# 
# You are given an array of characters arr that consists of sequences of characters 
# separated by space characters. Each space-delimited sequence of characters defines a word.
# 
# Implement a function reverseWords that reverses the order of the words in the 
# array in the most efficient manner.
# 
# Explain your solution and analyze its time and space complexities.
# 
# input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
#                 'm', 'a', 'k', 'e', 's', '  ',
#                 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
# 
# output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
#           'm', 'a', 'k', 'e', 's', '  ',
#           'p', 'e', 'r', 'f', 'e', 'c', 't' ]
# 
# Constraints:
# 
# [time limit] 5000ms
# 
# [input] array.character arr
# 
# 0 ≤ arr.length ≤ 100
# [output] array.character
# =============================================================================

def reverse_words(arr):
  #pass # your code goes here
  possition = [-1]
  length = len(arr)
  for i in xrange(length):
    if arr[i] == " ":
      possition.append(i)
  possition.append(length)
  
  
  wordList = []
  for i in xrange(1,len(possition)):
    wordList.append(arr[ possition[i-1]+1 : possition[i] ])
  
  result = []
  for i in xrange(len(wordList)-1,-1,-1):
    result += wordList[i]
    result.append(" ")
  result.pop()
  return result