#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List


class Solution:

    def isSafe(self,r:int,c:int,board: List[List[str]],n:int):
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
                if r - i >= 0 and c - i >= 0 and board[r-i][c-i] == 'Q':
                    return False
                if r - i >= 0 and c + i < n and board[r-i][c+i] == 'Q':
                    return False
            return True
               
            
    
    def findTruth(self,row:int,board: List[str],n:int):
        if row==n:
            self.results.append(["".join(i) for i in board])
            # print(board)
            return True

        temp = board[row]
        for col in range(n):
            
            if not self.isSafe(row,col,board,n):
                continue

            board[row] = f"{board[row][:col]}Q{board[row][col + 1:]}"
            self.findTruth(row+1,board,n)
            board[row]=temp

        return False
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results = []
        board:List[str] = ["."*n for _ in range(n)]
        self.findTruth(0,board,n)
        return self.results
        
        
        
        
        
        
# @lc code=end

