#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#

# @lc code=start
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


class Solution:
    @dataclass
    class Path:
        to:int
        color:bool
    
    def make_graph(self,redEdges:List[List[int]],blueEdges:List[List[int]],n:int): 
        self.graph:List[List[self.Path]]=[ [] for _ in range(n) ]
        for edges in redEdges:
            self.graph[edges[0]].append(self.Path(to=edges[1],color=False))
            
        for edges in blueEdges:
            self.graph[edges[0]].append(self.Path(to=edges[1],color=True))

        
            
    def dfs(self, current, current_stack: List[int],distance: int = 0):
        if self.distance[current.to]> distance or self.distance[current.to]==-1:
            self.distance[current.to] = distance
        for neighbor in self.graph[current.to]:
            print(neighbor.to," . ",current_stack)
            
            if current.color is None or current.color != neighbor.color:
                if neighbor.to in current_stack:
                    return
                current_stack.append(current.to)
                self.dfs(neighbor, distance=distance + 1,current_stack=current_stack)
        
 
    
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        self.distance = [-1 for _ in range(n)]
        self.make_graph(redEdges=redEdges,blueEdges=blueEdges,n=n)   
        self.dfs(self.Path(0,None),current_stack=[])
        return self.distance
        
        
        
#         3
# [[0,1],[0,2]]
# [[1,0]]
        
        
# @lc code=end

