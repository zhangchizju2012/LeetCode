#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 23:42:39 2017

@author: zhangchi
"""

# 大声说出来
# 用嘴跑例程

def calc_drone_min_energy(route):
  #pass # your code goes here

# That is, no energy was expended to place the drone at the starting point.
# [0,   2, 10] -> [3,   5,  0] energy_result = + 10, total_energy = 0
# [3,   5,  0] -> [9,  20,  6] energy_result = - 6, total_energy = 4 
  #total_energy = 0
  #output = 0
  #for i in xrange(1,len(route)):
  #  energy_result = route[i-1][2] - route[i][2]
  #  total_energy += energy_result
  #  if total_energy < 0:
  #    output = max(output, -total_energy)
  #return output
  highest = route[0][2]
  for i in xrange(1,len(route)):
    highest = max(route[i][2],highest)
  return highest - route[0][2]

# =============================================================================
# Drone Flight Planner
# 
# You’re an engineer at a disruptive drone delivery startup and your CTO asks you to come up with an efficient algorithm that calculates the minimum amount of energy required for the company’s drone to complete its flight. You know that the drone burns 1 kWh (kilowatt-hour is an energy unit) for every mile it ascends, and it gains 1 kWh for every mile it descends. Flying sideways neither burns nor adds any energy.
# 
# Given an array route of 3D points, implement a function calcDroneMinEnergy that computes and returns the minimal amount of energy the drone would need to complete its route. Assume that the drone starts its flight at the first point in route. That is, no energy was expended to place the drone at the starting point.
# 
# For simplicity, every 3D point will be represented as an integer array whose length is 3. Also, the values at indexes 0, 1, and 2 represent the x, y and z coordinates in a 3D point, respectively.
# 
# Explain your solution and analyze its time and space complexities.
# 
# Example:
# 
# input:  route = [ [0,   2, 10],
#                   [3,   5,  0],
#                   [9,  20,  6],
#                   [10, 12, 15],
#                   [10, 10,  8] ]
# 
# output: 5 # less than 5 kWh and the drone would crash before the finish
#           # line. More than `5` kWh and it’d end up with excess energy
# =============================================================================
