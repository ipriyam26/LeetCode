#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List


class Solution:

    
    def make_adjacency_list(self, arr:List[List[int]], n:int):
        adj = [[] for _ in range(n+1)]
        for relation in arr:
            adj[relation[1]].append(relation[0])
        return adj
                
    
    def dfs(self, current_node: int):
        self.visited[current_node] = 1
        for children in self.adj[current_node]:
            if self.visited[children] == 1:
                # print(f"Detected Cycle {children}")
                return False
            if self.visited[children] == 0 and not self.dfs(current_node=children):
                return False
        self.visited[current_node] = 2
        return True
        
                
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = [0 for _ in range(numCourses)]
        self.adj = self.make_adjacency_list(prerequisites, numCourses)
        return not any(self.visited[i] == 0 and not self.dfs(i) for i in range(numCourses))
        

        
# @lc code=end

