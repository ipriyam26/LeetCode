#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from typing import List


class Solution:
    
    #function to find maximum height of a tree
    def find_max_height(self, root: int,n: int) -> int:
        self.visited = [False] * n
        return self.dfs(root,0,0)
    
    def dfs(self,current:int,height:int,max_height:int) -> int:
        self.visited[current] = True
        if height > max_height:
            max_height = height
        for neighbor in self.graph[current]:
            if not self.visited[neighbor]:
                hh = self.dfs(neighbor,height+1,max_height)
                if hh > max_height:
                    max_height = hh
        return max_height
      
        
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        self.graph = [[] for _ in range(n)]
        for u,v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        min_height = self.find_max_height(0,n)
        min_node = [0]
        for i in range(1,n):
            temp = self.find_max_height(i,n)
            if temp<min_height:
                min_height=temp
                min_node.clear()
            if temp == min_height:
                min_node.append(i)
        return min_node
                
            
        

        
# @lc code=end

