#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 17:35:26 2017

@author: zhangchi
"""

def get_shortest_unique_substring(arr, str):
    checkLength = None
    dic = {}
    output = None
    for item in arr:
      dic[item] = 1
    for index, item in enumerate(str):
      if item in dic:
        dic.pop(item)
      if len(dic) == 0:
        checkLength = index + 1
        output = str[:index+1]
        break
    if checkLength is None:
      return ""
    start = 1
    checkLength -= 1
    while start + checkLength <= len(str):
      #print start
      if check(str[start:start+checkLength], arr):
        output = str[start:start+checkLength]
        checkLength -= 1
      else:
        start += 1
    return output
    
    
def check(str, arr):
    dic = {}
    for item in arr:
      dic[item] = 1
    for item in str:
      if item in dic:
        dic.pop(item)
    return len(dic) == 0
  
#arr = ['x','y','z']
#str = "xyyzyzyx"
#print get_shortest_unique_substring(arr, str)
      
  
  # pass # your code goes here
  # can you hear me?
  # i can hear you.
  # I can't hear you.
  # what broser do you use chrome
  # you can try Opera.
  # i can hear you.
  # you can try to download Opera, and i focus on the problems firstly
  # i check, i think it's ok
  # i use chrome before, sometimes it works while sometimes not. ok let me try opera