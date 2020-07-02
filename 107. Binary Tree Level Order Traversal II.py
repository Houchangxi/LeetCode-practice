#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:42:19 2020

@author: andrew
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         迭代进行queue 然后一个一个弹出 进行添加
        # from collections import deque
        # if not root: return []
        # queue = deque()
        # queue.appendleft(root)
        # res = []
        # while queue:
        #     tmp = []
        #     n = len(queue)
        #     for _ in range(n):
        #         node = queue.pop()
        #         tmp.append(node.val)
        #         if node.left:
        #             queue.appendleft(node.left)
        #         if node.right:
        #             queue.appendleft(node.right)
        #     res.insert(0, tmp)
        # return res

    
#     递归往下进行 由于结果是按照倒叙排列的 所以结果需要按照倒叙插入
        res = []
        def helper(root, depth):
            if not root: return 
            if depth == len(res):
                res.insert(0, [])
            res[-(depth+1)].append(root.val)
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        helper(root, 0)
        return res

