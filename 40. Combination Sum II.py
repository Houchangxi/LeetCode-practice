#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 17:09:05 2020

@author: andrew
"""
# DFS 解题
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        new_cand = sorted(candidates)
        ans = []
        length = len(candidates)
        curr = []
        def dfs (nums,target,s,curr,ans):

            if target == 0:
                ans_curr = sorted(curr)
                if ans_curr not in ans:
                    ans.append(ans_curr)
                return
            for i in range(s,length):
                num = nums[i]
                if target < num:
                    return 
                curr.append(num)
                dfs(nums,target - num,i+1,curr,ans)
                # dfs后抛出之前的num 然后继续循环
                curr.pop()
        dfs(new_cand,target,0,curr,ans)
        return ans