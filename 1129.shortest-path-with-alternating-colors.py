#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#

# @lc code=start
from dataclasses import dataclass
from typing import List, Tuple


class Solution:
    @dataclass
    class Path:
        to:int
        color:bool
    
    def make_graph(self,redEdges:List[List[int]],blueEdges:List[List[int]],n:int)->List[List[Path]]:
        
        graph=[ [] for _ in range(n) ]

        for edges in redEdges:
            graph[edges[0]].append(self.Path(to=edges[1],color=False))
            
        for edges in blueEdges:
            graph[edges[0]].append(self.Path(to=edges[1],color=True))
       
        return graph 
        
            
    def dfs(self,graph:List[List[Path]]):
        color = None
        stack = graph[0]
        visited = [0 for _ in range(len(graph))]
        run=1
        while stack:
            node = stack.pop(0)
            visited[node.to]=run
            run+=1
            if node.color != color:
                stack = graph[node.to] + stack
                
            
        
    
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = self.make_graph(redEdges=redEdges,blueEdges=blueEdges,n=n)        

        
        
        
        
        
        
# @lc code=end

