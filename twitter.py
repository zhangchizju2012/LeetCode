#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:59:34 2017

@author: zhangchi
"""

(1)

SELECT Departments.DEPT_NAME, IFNULL(Data.c, 0) AS n
FROM Departments
LEFT JOIN (SELECT DEPT_ID, COUNT(STUDENT_ID) AS c
FROM Students
GROUP BY DEPT_ID) Data
ON Departments.DEPT_ID = Data.DEPT_ID
ORDER BY n DESC, Departments.DEPT_NAME ASC

(2)

def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
    follow = set()
    twitter_list = {}
    for edge in followGraph_edges:
        if edge[0] == targetUser:
            follow.add(edge[1])
    for edge in likeGraph_edges:
        if edge[0] in follow:
            if edge[1] not in twitter_list:
                twitter_list[edge[1]] = 1
            else:
                twitter_list[edge[1]] += 1
    temp = []
    for item in twitter_list:
        if twitter_list[item] >= minLikeThreshold:
            temp.append([item,twitter_list[item]])
    temp.sort(key=lambda x:x[1],reverse=True)
    result = []
    for item in temp:
        result.append(item[0])
    return result

(3)

def  krakenCount(m, n):
    temp = [[1] * n for i in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            temp[i][j] = temp[i-1][j] + temp[i][j-1] + temp[i-1][j-1]
    return temp[m-1][n-1]