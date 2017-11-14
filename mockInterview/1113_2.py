#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:24:21 2017

@author: zhangchi
"""

def deletion_distance(str1, str2):
  #pass # your code goes here
  # dp[i][j] stands for the deletion_distance for str1[:i] and str2[:j]
  # between str1's substring constitute by the first i elemnts and 
  # str2's substring consititute by the first j elments.
  length1 = len(str1)
  length2 = len(str2)
  dp = [[0] * (length2+1) for _ in xrange(length1+1)]
  for i in xrange(length2+1):
    dp[0][i] = i
  for i in xrange(length1+1):
    dp[i][0] = i
  for i in xrange(1,length1+1):
    for j in xrange(1,length2+1):
      if str1[i-1] == str2[j-1]:
        dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1])
      else:
        dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)
  return dp[length1][length2]

str1 = "dog"
str2 = "frog"
print deletion_distance(str1, str2)
# can you hear me?
# no
# can you hear me?

# i can hear you.
# maybe you can use Opera.
# safari sometimes doesn't work.
# firework may work. chrome maybe better.
# trying chrome right now.

# now i can't see you and hear you.
# can you hear me?

# Opera works best, maybe you can download one now
# ok hold on a bit. feel free to start though

# ok

# i can hear you now.
# can you hear me?
# no I can't but that's okay. we will just continue this way
# fine.