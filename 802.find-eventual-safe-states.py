#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        empty_elements = [i for i in range(len(graph)) if graph[i]==[]]
        graph = [ element for element in graph if element ]
        ans = empty_elements.copy()
        while empty_elements:
            for i in range(len(graph)):
                graph[i] = list(set(graph[i]) - set(empty_elements))
            empty_elements = [i for i in range(len(graph)) if graph[i]==[]]
            ans+=empty_elements
            graph = [ element for element in graph if element ] 
        ans.sort()
        return   ans
                
he =        [[1,2],[2,3],[5],[0],[5],[],[]]
sol = Solution()
print(sol.eventualSafeNodes(he))
# @lc code=end

