#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:48:29 2020

@author: andrew
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # NESW
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        x,y,direction = 0,0,0
        
        for i in instructions:
            if i == "G":
                x += directions[direction][0]
                y += directions[direction][1]
            elif i == "L":
                direction = (direction+3)%4
            else:
                direction = (direction+1)%4
        # 机器人是否循环，主要看走完一个instructions后 机器人面对的方向 如果面对的方向和初始方向不同，那么就可以循环完成 或者 一个instructions后 回到原点
        return (x==0 and y==0) or direction != 0