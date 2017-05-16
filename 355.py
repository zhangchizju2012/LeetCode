#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:34:32 2017

@author: zhangchi
"""

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followRelation = {}
        self.twitterPost = {}
        self.time = 1
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId in self.twitterPost:
            self.twitterPost[userId].append([tweetId,self.time])
        else:
            self.twitterPost[userId] = [[tweetId,self.time]]
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        result = []
        temp = []
        temp.append(userId)
        if userId in self.followRelation:
            for item in self.followRelation[userId]:
                temp.append(item)
        for item in temp:
            if item in self.twitterPost:
                result += self.twitterPost[item]
        result.sort(key=lambda x:x[1],reverse=True)
        count = 0
        finalResult = []
        for item in result:
            if count < 10:
                count += 1
                finalResult.append(item[0])
            else:
                break
        return finalResult
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId != followerId: # followeeId & followerId can not be the same
            if followerId not in self.followRelation:
                self.followRelation[followerId] = {followeeId:1}
            else:
                self.followRelation[followerId][followeeId] = 1

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followRelation and followeeId in self.followRelation[followerId]:
            self.followRelation[followerId].pop(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)