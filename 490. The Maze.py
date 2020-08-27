#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:09:14 2020

@author: andrew
"""

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(maze)
        n = len(maze[0])
        
        stack = []
        seen = set()
        
#         队列记录走过到点不再重复走 memornazition 
        stack.append((start[0],start[1]))
        seen.add((start[0],start[1]))
#         进行遍历所有的点
        while stack:
            cur_i, cur_j = stack.pop()
            
            for d in directions:
                ni = cur_i
                nj = cur_j
#                 一个方向走到底，直到边界
                while 0<=ni<m and 0<=nj<n and maze[ni][nj] ==0:
                    ni += d[0]
                    nj += d[1]
#                     退回一步作为现在的坐标点
                ni -= d[0]
                nj -= d[1]
#                 此题关键是停下来的条件，只有到达maze的边界 才能停下来 所以上边的一直走到底然后判断是否到终点，如果到达停止
                if ni ==destination[0] and nj ==destination[1]:
                    return True
#         while继续循环下一个点，但之前判断这个点是否走过
                if (ni,nj) not in seen:
                    stack.append((ni,nj))
                    seen.add((ni,nj))
        return False