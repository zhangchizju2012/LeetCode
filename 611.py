#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:12:23 2017

@author: zhangchi
"""

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        if length < 3:
            return 0
        tempResult = []
        for i in xrange(length-2):
            # 把第一数固定住，然后后两个数由指针挪动来决定
            first = nums[i]
            # 两个指针挪过去
            pointA = i + 1
            pointB = i + 2
            count = 0
            while pointB < length:
                if first + nums[pointA] > nums[pointB]:
                    # 这个比较好理解，如果前两个数相加足够大，可以让后一个数再大一些
                    count += 1
                    pointB += 1
                else:
                    tempResult.append(count)
                    pointA += 1
                    count -= 1
                    # 为了减少循环次数，这里只改变pointA, pointB没变化，count -= 1的目的是，如果挪动
                    # pointA之后满足条件了的话，会在line30那里再把1加上
                    if pointA == pointB:
                    # 如果pointA == pointB, 有点像是从line24那里重新开始，pointA,pointB之间的距离还是1，
                    # 但是他们相对于line24已经同时往右平移了
                        pointB += 1
                        count = 0
            tempResult.append((count+1)*count/2)
            # pointB顶到最右端了，需要把n,n-1,n-2,...1都加上（因为pointA还没有到最后第二那里）
            # 但是pointB能到最右端说明此时pointA是可以任意移动的
        return tempResult, sum(tempResult)
        
s = Solution()
print s.triangleNumber([3,3,4,5,6,7,7,8,9,8,9,10,11,11,12,19,22,24,35,82,84])
                
            