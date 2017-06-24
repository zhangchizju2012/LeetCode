#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 16:48:40 2017

@author: zhangchi
"""

class Solution(object):
    # 复习，完全自己写的，这个应该算dfs,快很多，击败90%，之前10%都没有
    # 涉及到一串数字，一个一个循环过去的同时进行分类讨论的套路：301.py
    # 排列组合似乎也属于这个套路
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        stack = 0
        count = 0
        leftCount = 0
        rightCount = 0
        # 统计有效的对数，以及（和）的总数
        for item in s:
            if item == "(":
                stack += 1
                count += 1
                leftCount += 1
            elif item == ")":
                rightCount += 1
                if stack > 0:
                    stack -= 1
                    count += 1
                else:
                    pass
        self.number = (count - stack) // 2 # 应该留下的总对数
        self.length = len(s) 
        self.leftCanThrow = leftCount - self.number # 应该丢弃的左括号的总数
        self.rightCanThrow = rightCount - self.number # 应该丢弃的右括号的总数
        self.result = set()
        self.s = s
        self.helper("",0,0,0,0,0)
        return list(self.result)
        
        
    def helper(self,now,leftUsed,leftThrow,rightUsed,rightThrow,index):
        # leftUsed: 已经留下的左括号的数量
        # leftThrow: 已经丢弃的左括号的数量
        # 思路: 只想每个字符，都存在可以保留，可以丢弃的选项
        if index == self.length:
            self.result.add(now)
        else:
            item = self.s[index]
            if item == "(":
                if leftUsed < self.number:
                    self.helper(now+"(",leftUsed+1,leftThrow,rightUsed,rightThrow,index+1)
                if leftThrow < self.leftCanThrow:
                    self.helper(now,leftUsed,leftThrow+1,rightUsed,rightThrow,index+1)
            elif item == ")":
                if rightUsed < leftUsed and rightUsed < self.number:
                    self.helper(now+")",leftUsed,leftThrow,rightUsed+1,rightThrow,index+1)
                if rightThrow < self.rightCanThrow:
                    self.helper(now,leftUsed,leftThrow,rightUsed,rightThrow+1,index+1)
            else:
                self.helper(now+item,leftUsed,leftThrow,rightUsed,rightThrow,index+1)
                
s = Solution()
print s.removeInvalidParentheses("(a)())()")

"""
Created on Mon Jun  5 22:09:23 2017

@author: zhangchi
"""

class Solution(object):
    # 这个就是一个一个字符丢掉试试，比较二，且慢
    # bfs, a little bit slow, can be solved by dfs.
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        from Queue import Queue
        q = Queue()
        d = {}
        q.put(s)
        d[s] = 1
        while q.empty() is False:
            tempS = q.get()
            if self.checkValid(tempS) == True:
                if len(result) == 0:
                    result.append(tempS)
                else:
                    if len(tempS) == len(result[0]):
                        result.append(tempS)
                    else:
                        return result
            else:
                for i in xrange(len(tempS)):
                    if tempS[i] in "()":
                        changeS = tempS[:i] + tempS[i+1:]
                        if changeS not in d:
                            d[changeS] = 1
                            q.put(changeS)
        return result # for ['']
    
    def checkValid(self, s):
        count = 0
        for item in s:
            if item == "(":
                count += 1
            elif item == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0
        
s = Solution()
print s.removeInvalidParentheses("()())()")