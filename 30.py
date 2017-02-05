#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:28:17 2016

@author: zhangchi
"""

class Solution(object):
    '''
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word = words[0]
        length = len(word)
        number = len(words)
        tempwords = words[1:]
        words.remove(word)
        begin = 0
        result = []
        tempstr = s
        while word in tempstr:
            index = s.find(word,begin)
            temp = number - 1
            leftpoint = index
            rightpoint = index + length
            while temp > 0 and leftpoint >=0 and s[leftpoint-length:leftpoint] in words:
                words.remove(s[leftpoint-length:leftpoint])
                leftpoint = leftpoint - length
                temp = temp - 1                
            while temp > 0 and rightpoint + length <= len(s) and s[rightpoint:rightpoint+length] in words:
                words.remove(s[rightpoint:rightpoint+length])
                rightpoint = rightpoint + length
                temp = temp - 1
            if temp == 0:
                result.append(leftpoint)
            tempstr = tempstr[tempstr.find(word)+1:]
            begin = index + 1
            words = []
            for item in tempwords:
                words.append(item)
        return result
    '''
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_number = len(words)
        if word_number == 0:
            return []
        word_length = len(words[0])
        word = words[0]
        words.remove(word)
        words.sort()
        #先找到一个位置，然后在这个位置前后滑动窗口，maybe a better idea.
        
    '''
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Accepted, but too stupid, I can improve it.
        word_number = len(words)
        if word_number == 0:
            return []
        word_length = len(words[0])
        words.sort()
        result = []
        for i in range(len(s)-word_number*word_length+1):
            temp = s[i:i+word_number*word_length]
            temp_list = [temp[j:j+word_length] for j in range(0,word_number*word_length,word_length)]
            temp_list.sort()
            if temp_list == words:
                result.append(i)
        return result
    '''
    
            
S = Solution()
#s = "barfoobarthefoobarman"#这个问题无法解决 推广： 123421（每个数字表示一个word）这类无法解决
s = "wordgoodgoodgoodbestword"
words =["word","good","best","good"]
#words = ["foo","bar"]
#s = 'barfoothefoobarman'
#words = ["foo", "bar"]
print S.findSubstring(s, words)