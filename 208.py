#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 17:01:18 2017

@author: zhangchi
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []
        self.childrenValue = {} # key是字符，value是在self.children中所处的位置

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode("")
        
    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for item in word:
            if item in node.childrenValue:
                node = node.children[node.childrenValue[item]]
            else:
                return False
        if "" in node.childrenValue:
            return True
        else:
            return False
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for item in prefix:
            if item in node.childrenValue:
                node = node.children[node.childrenValue[item]]
            else:
                return False
        return True
        