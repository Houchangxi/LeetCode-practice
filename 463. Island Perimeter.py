#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 12:27:11 2020

@author: andrew
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        
        ans = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans +=4
                    
                    if i >0 and grid[i-1][j]==1:
                        ans -=2
                    if j >0 and grid[i][j-1]==1:
                        ans -=2
        return ans
    
#     本题就是找到方格做减法 只要相邻就减2