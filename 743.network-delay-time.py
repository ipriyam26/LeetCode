#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from queue import PriorityQueue
from typing import List, Tuple


class Solution:
    
    def make_adjacency_list(self, arr:List[List[int]], n:int)->List[List[Tuple[int, int]]]:
        self.adj = [[] for _ in range(n+1)]
        for relation in arr:
            print(f"Error at: {relation} ")
            self.adj[relation[0]].append(( relation[2],relation[1]))
        return self.adj
                
    def dijkstra(self, n:int, k:int)->int:
        distance = [float('inf')]*(n+1)
        visited = [False]*(n+1)
        distance[k]=0
        queue = PriorityQueue()
        queue.put((0,k))
        while queue:
            current:Tuple[int,int] = queue.get()
            visited[current[1]]=True
            while self.adj[current[1]]:
                next_node:Tuple[int,int] = self.adj[current[1]].pop(0)
                if not visited[next_node[1]]:
                    distance[next_node[1]] = min(distance[next_node[1]], distance[current[1]]+next_node[0])
                    queue.put((distance[next_node[1]], next_node[1]))
        return max(distance) if max(distance) != float('inf') else -1
            
            
        
        
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.make_adjacency_list(times, n)
        return self.dijkstra(n, k)
        

        
# @lc code=end

