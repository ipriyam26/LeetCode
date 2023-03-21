#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List


class Solution:

        class UnionFind:
            
            def __init__(self, size):
                self.count = size
                self.size = [1 for _ in range(size)]
                self.id = list(range(size))
            
            def find(self,p)-> int:
                root = p
                while self.id[root] != root:
                    root = self.id[root]
                
                #path compression
                while root != p:
                    temp = self.id[p]
                    self.id[p] = root
                    p = temp
                    
                return root
            
            def union(self, p, q) -> bool:
                rootP = self.find(p)
                rootQ = self.find(q)
                if self.isConnected(p, q):
                    return False
                if self.size[rootP] > self.size[rootQ]:
                    self.id[rootQ] = rootP
                    self.size[rootP] += self.size[rootQ]
                else:
                    self.id[rootP] = rootQ
                    self.size[rootQ] += self.size[rootP]
                self.count -= 1
                return True
            
            def getSize(self,p)-> int:
                return self.size[self.find(p)]
            
            def isConnected(self,p,q)-> bool:
                return self.find(p) == self.find(q)
            
            def getId(self,p)-> int:
                return self.id[p]
            
            def findLargestComponent(self) -> int:
                return self.find(self.size.index(max(self.size)))
            
            def getSizeOfLargestComponent(self) -> int:
                return max(self.size)
            
            def numberOfComponents(self) -> int:
                return self.count
            
            
        def longestConsecutive(self, nums: List[int]) -> int:
            
            
        
# @lc code=end

