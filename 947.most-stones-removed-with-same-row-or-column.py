#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start
from typing import List


class Solution:
    
    def makeAdjMatrix(self,data: List[List[int]]):
        self.adj = [[0 for _ in len(data)+1] for _ in len(data)+1]
        for stone in data:
            self.adj[stone[0]][stone[1]] = 1

    
    # def remove(self):
    #     for i,row in enumerate(self.adj):
    #         for j,col in enumerate(self.adj[i]):
            

    def removeStones(self, stones: List[List[int]]) -> int:
        # find matching row and column for each and remove them
        self.makeAdjMatrix()
        
        
        
        
        
# @lc code=end

