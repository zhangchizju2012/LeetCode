#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 17:43:21 2017

@author: zhangchi
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []
        self.childrenValue = {} # key是字符，value是在self.children中所处的位置

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode("")

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for item in word:
            if item in node.childrenValue:
                node = node.children[node.childrenValue[item]]
            else:
                newNode = TreeNode(item)
                node.childrenValue[item] = len(node.children)
                node.children.append(newNode)
                node = newNode
        if "" not in node.childrenValue:
            newNode = TreeNode("") # 用来表示一个string的结束
            node.childrenValue[""] = len(node.children)
            node.children.append(newNode)
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.helper(word, self.root)
        
    def helper(self, word, startNode):
        node = startNode
        for index, item in enumerate(word):
            if item == ".":
                for possibleNode in node.children:
                    if self.helper(word[index+1:],possibleNode):
                        return True
                return False # 所有可能性都不行，就该返回false了，不要忘了
            else:
                if item in node.childrenValue:
                    node = node.children[node.childrenValue[item]]
                else:
                    return False
        if "" in node.childrenValue:
            return True
        else:
            return False
        
w = WordDictionary()
w.addWord("a")
print w.search("a.")