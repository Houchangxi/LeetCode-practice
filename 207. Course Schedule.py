#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:54:00 2020

@author: andrew
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses =defaultdict(list)
        for i in prerequisites:
            courses[i[1]].append(i[0])
#         0 unknown 1 visiting 2 visited  此处为graph的课程做一个状态标记
        arr  =[0 for _ in range(numCourses)]
        for i in range(numCourses):
            if self.dfs(i,arr,courses):
                return False
        return True
    
    
    
#     判断是否为一个环 如果是环 则表示课程无法完成 
    def dfs(self,cur,arr,courses):
#         visited的状态可以认为是一个 memo的优化
        if arr[cur]==1: return True
        if arr[cur]==2: return False
#         标记为visiting 
        arr[cur] = 1
#     此处为递归去graph中查找 现在的课程下相连接的课程中 是否存在一个环如果有 则返回True
        for n in courses[cur]:
            if self.dfs(n,arr,courses):
                return True
#         标记为visited
        arr[cur] = 2
        return False
# 此题核心为 graph和dfs 去图中查找 是否存在环 如果存在环 则课程无法完成