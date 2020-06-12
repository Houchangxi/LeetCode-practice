#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:03:51 2020

@author: andrew
"""

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.source = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.source)
        self.source.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last_element, idx = self.source[-1] , self.dict[val]
            self.source[idx],self.dict[last_element]  = last_element,idx
            
            self.source.pop()
            del self.dict[val]
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return choice(self.source)
# 此题就是运用字典查找迅速的效率 来实现O（1）的   字典存储index list来存value

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()