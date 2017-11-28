#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 12:41:38 2017

@author: zhangchi
"""

import matplotlib.pyplot as plt
import numpy as np

class Node(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = "w"
        self.parent = 0
        self.d = 0
        self.index = 0
        self.children = []
        self.overlap_hv = 0
        self.overlap_vh = 0
        self.check = False
        
    def __str__(self):
        print self.index
        print self.children
        return "parent: " + str(self.parent)


def draw(nodes):
    fig = plt.figure()
    fig.set_size_inches(5, 5)
    plt.plot([item.x for item in nodes],[item.y for item in nodes], 'ro')
    
    ax = fig.add_subplot(1,1,1)              

    for index,node in enumerate(nodes):
        ax.annotate(index,xy=(node.x,node.y))                                        
    
    # major ticks every 20, minor ticks every 5                                      
    major_ticks = np.arange(0, 101, 20)                                              
    minor_ticks = np.arange(0, 101, 5)                                               
    
    ax.set_xticks(major_ticks)                                                       
    ax.set_xticks(minor_ticks, minor=True)                                           
    ax.set_yticks(major_ticks)                                                       
    ax.set_yticks(minor_ticks, minor=True)                                           
    
    # and a corresponding grid                                                       
    
    ax.grid(which='both')                                                            
    
    # or if you want differnet settings for the grids:                               
    ax.grid(which='minor', alpha=0.2)                                                
    ax.grid(which='major', alpha=0.5)   
    plt.show()
    
def generateAllPossibility(number):
    if number == 0:
        return []
    if number == 1:
        return [["hv"],["vh"]]
    temp = generateAllPossibility(number-1)
    result = []
    for item in temp:
        result.append(item+["hv"])
        result.append(item+["vh"])
    return result

def calculateDistance(a,b):
    return abs(a.x-b.x) + abs(a.y-b.y)

nodesValue = [[0,0],[0,90],[70,100],[100,55],[30,30],[30,70],[70,90],[70,30],[50,50],[45,0]]
nodes = [Node(item[0],item[1]) for item in nodesValue]
draw(nodes)

length = len(nodes)
edge = [[0] * length for _ in xrange(length)]

for i in xrange(length):
    for j in xrange(i+1,length):
        edge[i][j] = edge[j][i] = calculateDistance(nodes[i],nodes[j])
    edge[i][i] = 0

for i in xrange(length):
    nodes[i].d = edge[i][0]
    nodes[i].index = i

nodes[0].color = "b"
num = 1
length_mst = 0
while num < length:
    minDis = float('inf')
    for i in xrange(length):
        if nodes[i].color == "w" and nodes[i].d < minDis:
            minDis = nodes[i].d
            point = i
        elif nodes[i].color == "w" and nodes[i].d == minDis:
            if (abs(nodes[i].y - nodes[nodes[i].parent].y) > abs(nodes[point].y - nodes[nodes[point].parent].y)) or \
            ((abs(nodes[i].y - nodes[nodes[i].parent].y) == abs(nodes[point].y - nodes[nodes[point].parent].y)) and max(nodes[i].x,nodes[nodes[i].parent].x) > max(nodes[point].x,nodes[nodes[point].parent].x)):
                minDis = nodes[i].d
                point = i
                
    nodes[nodes[point].parent].children.append(point)
            
    length_mst += minDis
    nodes[point].color = "b"
    num += 1
    for i in xrange(length):
        if nodes[i].color == "w" and nodes[i].d > edge[i][point]:
            nodes[i].d = edge[i][point]
            nodes[i].parent = point
        elif nodes[i].color == "w" and nodes[i].d == edge[i][point]:
            if (abs(nodes[i].y - nodes[nodes[i].parent].y) < abs(nodes[i].y - nodes[point].y)) or \
            ((abs(nodes[i].y - nodes[nodes[i].parent].y) == abs(nodes[i].y - nodes[point].y)) and max(nodes[i].x,nodes[nodes[i].parent].x) < max(nodes[i].x,nodes[point].x)):
                nodes[i].parent = point
                
for index, node in enumerate(nodes):
    print node
                

def helper(s,e):
    start = nodes[s]
    #nodelist = [nodes[i] for i in start.children]
    nodelist = []
    for i in start.children:
        if nodes[i].check is False:
            helper(i,start.index)
        nodelist.append(nodes[i])
    end = nodes[e]
    
    positionsList = generateAllPossibility(len(nodelist))
    
    nodelist.append(end)
    for choice in ['hv','vh']:
        maxOverlap = 0
        for positions in positionsList:
            #positions.append(choice)
            overlap = 0
            left = right = start.x
            up = down = start.y
            for node, position in zip(nodelist, positions+[choice]):
                if position[0] == "h":
                    if node.y > start.y:
                        overlap += min(node.y-start.y,up-start.y)
                        up = max(up, node.y)
                    else:
                        overlap += min(start.y-node.y,start.y-down)
                        down = min(down,node.y)
                    if node != nodelist[-1]:
                        overlap += node.overlap_hv
                else:
                    if node.x > start.x:
                        overlap += min(node.x-start.x,right-start.x)
                        right = max(right, node.x)
                    else:
                        overlap += min(start.x-node.x,start.x-left)
                        left = min(left,node.x)
                    if node != nodelist[-1]:
                        overlap += node.overlap_vh
            maxOverlap = max(maxOverlap, overlap)
        if choice == "hv":
            start.overlap_vh = maxOverlap
        else:
            start.overlap_hv = maxOverlap
        #print choice + ": " + str(maxOverlap)
        
    start.check = True

helper(0,0)
print "-----------------------------"
for index, node in enumerate(nodes):
    print node
    print node.overlap_hv
    print node.overlap_vh
    print "------"