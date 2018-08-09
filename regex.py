#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 12:11:21 2018

@author: zhangchi
"""

# regular expression practice

import re

def check(pattern, content):
    result = re.search(pattern, content)
    if result:
        print result.group()
        #print result.groups()
    
# 0. example
print 'Question: 0'
content = 'Hello 1234567 is a number. Regex String'
pattern = 'Hello \d+.*String'
check(pattern, content)
    
# 1. Write a Python program to check that a string contains only a certain set 
# of characters (in this case a-z, A-Z and 0-9)
print 'Question: 1'
content = 'Hello'#'Hello 123' # 'Hello'
pattern = '^[a-zA-Z0-9]+$'
check(pattern, content)

# 2. Write a Python program that matches a string that has an a 
# followed by zero or more b's.
print 'Question: 2'
content = 'dgabcab'#'Hello 123' # 'Hello'
pattern = 'ab*'
check(pattern, content)

# 3. Write a Python program that matches a string that 
# has an a followed by one or more b's.
print 'Question: 3'
content = 'dgabcab'#'Hello 123' # 'Hello'
pattern = 'ab+'
check(pattern, content)

# *** 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
print 'Question: 4'
content = 'dgabbab'#'Hello 123' # 'Hello'
pattern = '(ab{0,1}$)|(ab{0,1}[^b])'
check(pattern, content)

# 7. Write a Python program to find sequences of lowercase letters joined with a underscore.
print 'Question: 5'
content = 'c dgab_abb d'#'Hello 123' # 'Hello'
pattern = '[a-z]*_[a-z]*'
check(pattern, content)
# *** 允许abc_, _abc, abc_abc, 不允许 _ 应该怎么写