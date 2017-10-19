#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:44:12 2017

@author: zhangchi
"""

def game(eachLine):
    dic = {}
    dic['FB, F'] = "Homerun"
    dic['C, S'] = "Hit"
    dic['FB, S'] = "Strike"
    dic['C, F'] = "Strike"
    run = 0
    out = 0
    strike = 0
    strike_inRow = 0
    hit = 0
    hit_inRow = 0
    for item in eachLine:
        if dic[item] == "Hit":
            strike = 0
            strike_inRow = 0
            hit += 1
            hit_inRow += 1
            if hit_inRow >= 4:
                run += 1
                hit -= 1 #
                hit_inRow -= 1
                #hit_inRow = max(hit_inRow-4,0) #
        elif dic[item] == "Homerun":
            strike_inRow = 0
            hit_inRow = 0
            run = run + hit + 1
            hit = 0
        elif dic[item] == "Strike":
            strike_inRow += 1
            hit_inRow = 0
            strike += 1
            if strike_inRow >= 3:
                #strike_inRow = 3
                out += 1
        if out >= 3:
            return run
    return run
        
def main():
    #File = open("PracticeInput-3.txt")
    File = open("Little-league-simulation_InputForSubmission_2.txt")
    for line in File:
        eachLine = line.strip()[2:-2].split("), (")
        print game(eachLine)
        
main()

        