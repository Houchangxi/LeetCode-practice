#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:37:32 2020

@author: andrew
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        ans = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
#             注意这块 node有左子树 把根压入stack中 所以 在pop的时候 是获取的 最左子节点的 根节点 
            node = stack.pop() #  此处pop出来的数 就是最左子节点
            ans.append(node.val)
            node = node.right
        return ans

#         inorder 遍历记住一个句话  一直想做走 走到最左边
#         关键点是 走到最左后如何回到上一个层的root节点

#    此处确实容易混淆 https://www.youtube.com/watch?v=ZtCeAsWfGKA&t=2508s  