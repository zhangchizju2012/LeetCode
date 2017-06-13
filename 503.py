#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:31:44 2017

@author: zhangchi
"""

class Solution(object):
    # 复习496，跟496的重点部分基本上是一样的，只是这里的数组是环形的，而且元素可能会重复
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        stack = [(-1,float('inf'))]
        dic = {}
        # 第一步骤处理跟496一致，只是此时stack里存的东西是（index,item），之所以要保留index是因为此时元素可能重复
        # 所以在建立dict的时候应该用index作为key，保存item是为了进行值比较，这部分跟496一样
        for index,item in enumerate(nums):
            while item > stack[-1][1]:
                dic[stack.pop()[0]] = item
            stack.append((index,item))
        # 这里是为了配合数组是环形的这一特点，（像解决[1,2,3,2,1]这一问题），第二次循环数组
        # 需要再把数组循环到最大值这里，到了最大值之后就没有必要再循环了，因为此时stack剩下的只有最大值（但可能有多个最大值）
        # 此处让这前已经建立好的部分dict的key-value对进行了再一次的赋值，但是赋值跟之前的一样，不影响结果
        # 可以避免这一重新赋值行为，但是没有必要，似乎只能多了一些判断，也不能降低复杂度只能增加复杂度
        for index,item in enumerate(nums):
            if index <= stack[1][0]:
                while item > stack[-1][1]:
                    dic[stack.pop()[0]] = item
                stack.append((index,item))
        # 因为再次循环又到了最大值这里，所以最大值又一次被push到stack里了，但实际上是重复的，所以pop掉
        stack.pop()
        # 剩下的全部都是最大值，都赋值为 -1
        for index in xrange(1,len(stack)):
            dic[stack[index][0]] = -1

        result = []
        for index in xrange(len(nums)):
            result.append(dic[index])
        return result
        
s = Solution()
print s.nextGreaterElements([1,2,3,2,1])
            