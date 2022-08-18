#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from typing import List


class Solution:
    
    def dfs(self,current_node):
        self.visited[current_node] = True
            
        for nodes in range(self.length):
            if self.isConnected[current_node][nodes] and not self.visited[nodes]:
                self.dfs(nodes)
        
            
            
            
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.length = len(isConnected)
        self.isConnected = isConnected
        self.visited = [False] * self.length
        
        result = 0
        for i in range(self.length):
            if not self.visited[i]:
                self.dfs(i)
                result += 1
        return result
        
        
        
        
# @lc code=end

