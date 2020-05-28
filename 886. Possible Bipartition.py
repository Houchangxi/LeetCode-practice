#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:12:22 2020

@author: andrew
"""

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N==1 or not dislikes:
            return True
        
        self.GREEN,self.RED,self.NOT_COLOR = 1,-1,0
        self.dislikes_table = defaultdict(list)
        self.color_table = [self.NOT_COLOR for _ in range(N+1)]
        
        for u,v in dislikes:
            self.dislikes_table[u].append(v)
            self.dislikes_table[v].append(u)
        
        for person_id in range(1,N+1):
            if self.color_table[person_id] == self.NOT_COLOR and (not self.helper(person_id,self.GREEN)):
                return False
        return True
    
    
    
    
    def helper(self, person_id, COLOR):
        self.color_table[person_id] = COLOR
        
        for other_id in self.dislikes_table[person_id]:
            if self.color_table[other_id] == COLOR:
                print('from here')
                return False
            if self.color_table[other_id] == self.NOT_COLOR and (not self.helper(other_id,-COLOR)):
                return False
        return True
    
#     此题就是要标记 不同人的颜色 如果出现颜色冲突 就返回False 如果能够实现所有的人都可以划分为不同颜色 那么就是True 
#     详见：https://leetcode.com/problems/possible-bipartition/discuss/654955/Python-sol-by-DFS-and-coloring.-w-Graph