#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:55:14 2020

@author: andrew
"""

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        visited = [0]*N
        ans = 0

        def helper(M,visited,ind):
            for j in range(N):
                if M[ind][j] ==1 and visited[j] == 0 :
                    visited[j] =1
                    helper(M,visited,j)

        for i in range(N):
            if visited[i] == 0:
                helper(M,visited,i)
                ans+=1
        return ans
# 需要注意 这个矩阵是一个 N*N的矩阵，如果visited==0 就意味着发现一个有可能的新朋友圈，启动helper，helper为dps 根据朋友圈的定义等于1的人 都在visited的状态表里标记，循环vistited 只要遇到0 就表明上一个dps 没发现的朋友圈