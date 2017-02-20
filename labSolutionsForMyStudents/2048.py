#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:02:19 2017

@author: zhangchi
"""
import random

def merge(tempRow):
    outputRow = []
    i = 0
    while i < len(tempRow)-1:
        if tempRow[i] == tempRow[i+1]:
            outputRow.append(tempRow[i]*2)
            i = i + 2
        else:
            outputRow.append(tempRow[i])
            i = i + 1
    if i == len(tempRow)-1:
        outputRow.append(tempRow[i])
    for i in range(4-len(outputRow)):
        outputRow.append(0)
    return outputRow
    
def move(rows, direction):
    if direction == 'a':
        outputRows = []
        for row in rows:
            tempRow = []
            for item in row:
                if item != 0:
                    tempRow.append(item)
            outputRow = merge(tempRow)
            #print(outputRow)
            outputRows.append(outputRow)
    elif direction == 'd':
        outputRows = []
        for row in rows:
            tempRow = []
            for i in range(4):
                if row[3-i] != 0:
                    tempRow.append(row[3-i])
            temp = merge(tempRow)
            outputRow = []
            for i in range(4):
                outputRow.append(temp[3-i])
            #print(outputRow)
            outputRows.append(outputRow)
    elif direction == 'w':
        outputRows = [[],[],[],[]]
        for i in range(4):
            tempRow = []
            for j in range(4):
                if rows[j][i] != 0:
                    tempRow.append(rows[j][i])
            temp = merge(tempRow)
            for k in range(4):
                outputRows[k].append(temp[k])
    elif direction == 's':
        outputRows = [[],[],[],[]]
        for i in range(4):
            tempRow = []
            for j in range(4):
                if rows[3-j][i] != 0:
                    tempRow.append(rows[3-j][i])
            temp = merge(tempRow)
            for k in range(4):
                outputRows[3-k].append(temp[k])
    return outputRows

def begin():
    temp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    seed = random.randint(0,15)
    temp[seed//4][seed%4] = 2
    seed_2 = random.randint(0,15)
    while seed_2 == seed:
        seed_2 = random.randint(0,15)
    temp[seed_2//4][seed_2%4] = 2
    return temp

def addNumber(origin):
    seed = random.randint(0,9)
    if seed >= 1:
        temp = 2
    else:
        temp = 4
    count = 0
    for row in origin:
        for item in row:
            if item == 0:
                count = count + 1
    seed_2 = random.randint(0,count-1)
    count_again = 0
    for i in range(4):
        for j in range(4):
            if count_again == seed_2 and origin[i][j] == 0:
                origin[i][j] = temp
                count_again = count_again + 1
            if origin[i][j] == 0:
                count_again = count_again + 1
    return origin
        
#move([[0,8,2,16],[4,2,2,8],[0,8,8,8],[4,8,2,8]],'down')
origin = begin()
for row in origin:
    print(row)
while True:    
    direction = input('next move: ')
    if direction == 'q':
        break
    after = move(origin,direction)
    origin = addNumber(after)
    for row in origin:
        print(row)