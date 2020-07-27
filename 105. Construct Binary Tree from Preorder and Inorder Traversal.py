#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:50:06 2020

@author: andrew
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        rootval = preorder[0]
        root = TreeNode(rootval)
        inorderindex = inorder.index(rootval)

        root.left = self.buildTree(preorder[1:inorderindex+1],inorder[:inorderindex])
        root.right = self.buildTree(preorder[inorderindex+1:],inorder[inorderindex+1:])

        return root