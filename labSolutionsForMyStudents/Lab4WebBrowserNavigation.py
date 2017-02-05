#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 14:04:38 2017

@author: zhangchi
"""
"""
class Stack:
    
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        
    def pop(self):
        return self.__items.pop()
    
    def peek(self):
        return self.__items[len(self.__items)-1]
    
    def is_empty(self):
        return len(self.__items) == 0
    
    def size(self):
        return len(self.__items)
"""       
stack1 = []
stack2 = []
stack1.append("www.cs.ualberta.ca")
print "current page: " + stack1[-1]
while(True):
    user_input = raw_input("Enter: ")
    if user_input != "<" and user_input != ">":
        if len(stack2)>0 :# should delete memory in stack2
            stack2 = []
        stack1.append(user_input)
        print "current page: " + user_input
    elif user_input == "<":    
        if len(stack1)>1:
            item = stack1.pop()
            stack2.append(item)
            print "current page: " + stack1[-1]
        else:
            print user_input + " is an invalid action"
    elif user_input == ">":
        if len(stack2)>0:
            item = stack2.pop()
            stack1.append(item)
            print "current page: " + item
        else:
            print user_input + " is an invalid action"
"""
# version 1
# pass eclass, but still exists problems
stack1 = []
stack2 = []
last_user_input = None
stack1.append("www.cs.ualberta.ca")
print "current page: " + stack1[-1]
while(True):
    user_input = raw_input("Enter: ")
    if user_input != "<" and user_input != ">":
        if last_user_input == "<":
            stack2 = []
        stack1.append(user_input)
        print "current page: " + user_input
    elif user_input == "<":    
        if len(stack1)>1:
            item = stack1.pop()
            stack2.append(item)
            print "current page: " + stack1[-1]
        else:
            print user_input + " is an invalid action"
    elif user_input == ">":
        try:
            item = stack2.pop()
            stack1.append(item)
            print "current page: " + item
        except:
            print user_input + " is an invalid action"
    last_user_input = user_input
"""