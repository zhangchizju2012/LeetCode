#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 10:12:37 2017

@author: zhangchi
"""

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        result = []
        sx = float('inf')
        bx = -float('inf')
        sy = float('inf')
        by = -float('inf')
        for item in points:
            if item.x < sx:
                sx = item.x
                sxl = [item]
            elif item.x == sx:
                sxl.append(item)
            if item.y < sy:
                sy = item.y
                syl = [item]
            elif item.y == sy:
                syl.append(item)
            if item.x > bx:
                bx = item.x
                bxl = [item]
            elif item.x == bx:
                bxl.append(item)
            if item.y > by:
                by = item.y
                byl = [item]
            elif item.y == by:
                byl.append(item)
         
        for item in sxl:
            if item not in result:
                result.append(item)
        for item in syl:
            if item not in result:
                result.append(item)
        for item in bxl:
            if item not in result:
                result.append(item)
        for item in byl:
            if item not in result:
                result.append(item)
        return result
        
s = Solution()
print s.outerTrees()

#==============================================================================
# 587. Erect the Fence Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 227
# Total Submissions: 1016
# Difficulty: Hard
# Contributors:
# vishal51
# There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.
# 
# Example 1:
# Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# Explanation:
# 
# Example 2:
# Input: [[1,2],[2,2],[4,2]]
# Output: [[1,2],[2,2],[4,2]]
# Explanation:
# 
# Even you only have trees in a line, you need to use rope to enclose them. 
# Note:
# 
# All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
# All input integers will range from 0 to 100.
# The garden has at least one tree.
# All coordinates are distinct.
# Input points have NO order. No order required for output.
# Subscribe to see which companies asked this question.
# 
# 1. Solution 1
# Java Solution, Convex Hull Algorithm - Gift wrapping aka Jarvis march
# There are couple of ways to solve Convex Hull problem. https://en.wikipedia.org/wiki/Convex_hull_algorithms
# The following code implements Gift wrapping aka Jarvis march algorithm and also added logic to handle case of multiple Points in a line because original Jarvis march algorithm assumes no three points are collinear.
# It also uses knowledge in this problem https://leetcode.com/problems/convex-polygon . Disscussion: https://discuss.leetcode.com/topic/70706/beyond-my-knowledge-java-solution-with-in-line-explanation
# 
# public class Solution {
#     public List<Point> outerTrees(Point[] points) {
#         Point first = points[0];
#         int firstIndex = 0;
#         // Find the leftmost point
#         for (int i = 0; i < points.length; i++) {
#             Point point = points[i];
#             if (point.x < first.x) {
#                 first = point;
#                 firstIndex = i;
#             }
#         }
#         
#         Set<Point> answer = new HashSet<>();
#         Point cur = first;
#         int curIndex = firstIndex;
#         answer.add(first);
#         
#         do {
#             Point next = points[0];
#             int nextIndex = 0;
#             for (int i = 1; i < points.length; i++) {
#                 if (i == curIndex) continue;
#                 Point p = points[i];
#                 int cross = crossProductLength(p, cur, next);
#                 if (nextIndex == curIndex || cross > 0 ||
#                         // Handle multi points in a line
#                         (cross == 0 && distance(p, cur) > distance(next, cur))) {
#                     next = p;
#                     nextIndex = i;
#                 }
#             }
#             // Handle multi points in a line
#             for (int i = 0; i < points.length; i++) {
#                 Point p = points[i];
#                 int cross = crossProductLength(p, cur, next);
#                 if (i != curIndex && cross == 0) {
#                     answer.add(p);
#                 }
#             }
# 
#             cur = next;
#             curIndex = nextIndex;
#         } while (curIndex != firstIndex);
#         
#         return new ArrayList<>(answer);
#     }
#     
#     private int crossProductLength(Point A, Point B, Point C) {
#         // Get the vectors' coordinates.
#         int BAx = A.x - B.x;
#         int BAy = A.y - B.y;
#         int BCx = C.x - B.x;
#         int BCy = C.y - B.y;
#     
#         // Calculate the Z coordinate of the cross product.
#         return (BAx * BCy - BAy * BCx);
#     }
# 
#     private int distance(Point p1, Point p2) {
#         return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
#     }
# }
# 
# 
# 2. Solution 2
# Python, AM Chain with Explanation
# Based on the formula for the signed area of a triangle, we can find whether a triangle PQR has vertices which are counter-clockwise (sign 1), collinear (sign 0), or clockwise (sign -1).
# 
# We will now perform the AM-Chain algorithm for finding the lower and upper hulls which together form the convex hull of these points.
# 
# To find the lower hull of points, we process the points in sorted order. Focus on the function drive. Our loop invariant is that we started the function drive with a lower hull, and we return a lower hull. This answer must include the new right-most point r as it cannot be contained by some points below it. During the while loop, whenever our last turn XYZ was clockwise, the middle point Y cannot be part of the lower hull, as it is contained by WXZ (where W is the point in the hull before X.)
# 
# We can do this process again with the points sorted in reverse to find the upper hull. Both hulls combined is the total convex hull as desired.
# 
# def outerTrees(self, A):
#     def sign(p, q, r):
#         return cmp((p.x - r.x)*(q.y - r.y), (p.y - r.y)*(q.x - r.x))
#     
#     def drive(hull, r):
#         hull.append(r)
#         while len(hull) >= 3 and sign(*hull[-3:]) < 0:
#             hull.pop(-2)
#         return hull
#     
#     A.sort(key = lambda p: (p.x, p.y))
#     lower = reduce(drive, A, [])
#     upper = reduce(drive, A[::-1], [])
#     return list(set(lower + upper))
#==============================================================================
