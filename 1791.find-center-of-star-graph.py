#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start
from typing import List


class Solution:

                
    
        def findCenter(self, edges: List[List[int]]) -> int:
            n = len(edges)+1
            count = [0 for _ in range(n+1)]
            for relation in edges:
                count[relation[0]]+=1
                count[relation[1]]+=1
            return count.index(n-1)
            
            

        
# @lc code=end

