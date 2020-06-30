#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:59:44 2020

@author: andrew
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         m = len(board)
#         n = len(board[0])
#         dire = [(1,0),(-1,0),(0,1),(0,-1)]
#         ans = set()
#         def helper(word,i,j,ind,dp):
#             if len(word) ==ind:
#                 return True
#             if i<0 or i>=m or j<0 or j >=n or board[i][j]!=word[ind]:
#                 return False
#             tmp = dp[i][j]
#             dp[i][j] = ''
#             res = helper(word,i+dire[0][0],j+dire[0][1],ind+1,dp) or helper(word,i+dire[1][0],j+dire[1][1],ind+1,dp) or helper(word,i+dire[2][0],j+dire[2][1],ind+1,dp) or helper(word,i+dire[3][0],j+dire[3][1],ind+1,dp)
#             dp[i][j] = tmp
            
#             return res
        
#         for i in range(m):
#             for j in range(n):
#                 for word in words:
#                     if helper(word,i,j,0,board):
#                         ans.add(word)
#         return ans

# 传统的DFS解决问题 这个算法可以获得正确解，但是time limited 过不了
# 所以采用了下边的Tire 和 DFS方法 进行了优化
        
        ## RC ##
		## APPROACH : TRIE + DFS ##
		## LOGIC ##
		#	1. build trie with all words list
		#	2. start scanning matrix, move in all four directions and check if such combination exists in the trie
		#	3. make sure you donot return when result is found ( case: words = [cat, cattle ] )
		
        ## TIME COMPLEXICITY : O(M(4x3^(L-1))) ## (M is the number of cells in the board and L is the maximum length of words.)
		## SPACE COMPLEXICITY : O(N) ##
	    
        def dfs(i, j, curr, currNode):
            ch = board[i][j]
            if( ch not in currNode.children or (i, j) in visited ):
                return
            if currNode.children[ch].endOfWord:
                res.add(curr)
                # return                            # edge case
            visited.add((i,j))
            for x,y in directions:
                if 0 <= i + x < m and 0 <= j + y < n:
                    dfs( i + x, j + y, curr + board[i + x][j + y], currNode.children[ch])
            visited.remove((i,j))   # edge case
        
        # buid trie data structure
        my_trie = Trie()
        [ my_trie.insert(word) for word in words ]
        rootNode = my_trie.get_rootNode()
        
        m, n = len(board), len(board[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        res = set()                     
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = set()
                dfs(i, j, board[i][j], rootNode)
        return res
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.rootNode = TrieNode()
    
    def get_rootNode(self):
        return self.rootNode
    
    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        currNode = self.rootNode
        for idx, ch in enumerate(word):
            if( ch not in currNode.children ):
                currNode.children[ch] = TrieNode()
            currNode = currNode.children[ch]        
        currNode.endOfWord = True