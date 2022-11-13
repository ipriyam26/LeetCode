#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List


class Solution:

    def isSafe(self,row:int,col:int,board: List[List[str]],N:int):
        
        for item in board:
            if item[col] == "Q":
                return False

        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if board[i][j]=="Q":
                return False

        return all(board[i][j] != "Q" for i, j in zip(range(row,N), range(col,-1,-1)))
               
            
    
    def findTruth(self,row:int,board: List[List[str]],n:int):
        if row==n:
            return True
        
        for col in range(n):
            
            if not self.isSafe(row,col,board):
                continue
            
            board[row][col] ='Q'
            if self.findTruth(row+1,board):
                return True
            
            board[row][col]="."
        
        return False
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board:List[List[str]] = [["." for _ in range(n)] for _ in range(n)]
        
        
        
        
        
        
# @lc code=end

