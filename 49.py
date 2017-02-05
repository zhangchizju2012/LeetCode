#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:18:52 2016

@author: zhangchi
"""
# 一步一步简介并提高效率，都是自己写的
class Solution(object):
    '''
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionaryList = []
        stringList = []
        for item in strs:
            temp_dict = {}
            itemLength = len(item)
            for i in range(itemLength):
                if item[i] in temp_dict.keys():
                    temp_dict[item[i]] = temp_dict[item[i]] + 1
                else:
                    temp_dict[item[i]] = 1
            index = 0
            label = False
            for dictionary in dictionaryList:
                if dictionary == temp_dict:
                    stringList[index].append(item)
                    label = True
                    break
                index = index + 1
            if label == False:
                dictionaryList.append(temp_dict)
                stringList.append([item])
        return stringList
    ''' 
    '''
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionaryList = []
        stringList = []
        for item in strs:
            temp_dict = {}
            itemLength = len(item)
            for i in range(itemLength):
                if item[i] in temp_dict.keys():
                    temp_dict[item[i]] = temp_dict[item[i]] + 1
                else:
                    temp_dict[item[i]] = 1
            if temp_dict in dictionaryList:
                stringList[dictionaryList.index(temp_dict)].append(item)
            else:
                dictionaryList.append(temp_dict)
                stringList.append([item])
        return stringList
    '''
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}
        for item in strs:
            sortstr = ''.join(sorted(item))
            #if sortstr in dictionary.keys():#加上.keys()就会runtime error,但效果是一样的！！！
            if sortstr in dictionary:
                dictionary[sortstr].append(item)
            else:
                dictionary[sortstr] = [item]
        return dictionary.values()

a = ["eat", "tea", "tan", "ate", "nat", "bat"]
#a = []
S = Solution()
print S.groupAnagrams(a)