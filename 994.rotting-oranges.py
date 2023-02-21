#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from itertools import product
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue= []
        n,m = len(grid),len(grid[0])
        for i, j in product(range(n),range(m)):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # Lets do level order traversal and count number of levels unitll queue is empty
        
        levels = 0
        while queue:
            levels+=1
            for _ in range(len(queue)):
                i,j = queue.pop(0)
                # lets check all directions to see presence of any rotten
                for dx,dy in directions:
                    if 0<=i+dx<n and 0<=j+dy<m and grid[i+dx][j+dy]==1:
                        fresh-=1
                        grid[i+dx][j+dy]=2
                        queue.append((i+dx,j+dy))
        return -1 if fresh != 0 else max(levels-1, 0)
 
                
        
# @lc code=end

