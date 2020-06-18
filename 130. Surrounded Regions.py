#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:01:43 2020

@author: andrew
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
#         优化方案1、可以直接从边缘进行loop 用dfs去深度优先递归，找到为O的改变标记为E 然后全部循环完成后，原来数组的O转变为X 标记的E转变成O 即为结果
# 以下算法是将整个矩阵遍历，时间复杂度高 不如优化方案只便利边界点， 但以下方法是应用于大部分矩阵地图的题 可供参考
        if len(board) <1:
            return board
        di = [(1,0),(-1,0),(0,1),(0,-1)]
        n = len(board)
        m = len(board[0])
        
        def helper(di,i,j,positions,board,n,m):
            
            if i < 0 or i >= n:
                return 
            if j < 0 or j >= m:
                return 
            if board[i][j] == 'X':
                return 
            if board[i][j] == 'O':
                positions.add((i,j))
                board[i][j] = '#'
                for p in di:
                    helper(di,i+p[0],j+p[1],positions,board,n,m)
        edge= []
        edge +=[(i,0) for i in range(n)]
        edge +=[(i,m-1) for i in range(n)]
        edge +=[(0,j) for j in range(m)]
        edge +=[(n-1,j) for j in range(m)]
        for i in range(n):
            for j in range(m):
                positions = set()
                if board[i][j] == 'X':
                    continue
                helper(di,i,j,positions,board,n,m)
                if len(positions) >0:
                    flag = False
                    for k in positions:
                        if k in edge:
                            flag = True
                            break
                    if flag:
                        continue
                    else:
                        for k in positions:
                            board[k[0]][k[1]] = 'X'

        for i in range(n):
            for j in range(m):
                if board[i][j]=='#':
                    board[i][j]='O'