#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        A = set()
        B = set()
        stack = []
        visited = [False for _ in range(len(graph) + 1)]
        for i in range(len(graph)):
            if visited[i]:
                continue
            stack.append(i)
            while stack:
                element = stack.pop(0)
                if visited[element]:
                    continue
                visited[element] = True
                if(element in A):
                    for n in graph[element]:
                        if n in A:
                            return False
                        else:
                            B.add(n)
                        stack.append(n)
                elif element in B:
                    for n in graph[element]:
                        if n in B:
                            return False
                        else:
                            A.add(n)
                        stack.append(n)
                else:
                    A.add(element)
                    for n in graph[element]:
                        B.add(n)
                        stack.append(n)
                
        return True
                
# he = [[1,3],[0,2],[1,3],[0,2]]
# sol = Solution()
# print(sol.isBipartite(he))

# @lc code=end

