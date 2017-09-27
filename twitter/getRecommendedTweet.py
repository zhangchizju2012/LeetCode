#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 01:21:45 2017

@author: zhangchi
"""

def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
    follow_set = set() # the list for the people targetUser follows
    twitter_list = {} # key: candidate twitter; value: number of likes
    temp = []
    result = []
    for edge in followGraph_edges:
        if edge[0] == targetUser:
            follow_set.add(edge[1])
    for edge in likeGraph_edges:
        if edge[0] in follow_set:
            if edge[1] not in twitter_list:
                twitter_list[edge[1]] = 1
            else:
                twitter_list[edge[1]] += 1
    for item in twitter_list:
        if twitter_list[item] >= minLikeThreshold: # get twitter satisfies minLikeThreshold
            temp.append([item,twitter_list[item]])
    temp.sort(key=lambda x:x[1],reverse=True) # sort by likes
    for item in temp:
        result.append(item[0]) # get final result
    return result
    
    