import itertools
from typing import List


class Solution:

    def flipZeros(self,row:List[int],col:List[int]):
        for i in range(self.matrix):
            for j in col:
                self.matrix[i][j] =0
        for j in range(self.matrix[0]):
            for i in row:
                self.matrix[i][j]
       
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix= matrix
        row = set()
        col = set()
        for i, j in itertools.product(range(len(matrix)), range(len(matrix[0]))):
            if matrix[i][j]==0:
                row.add(i)      
                col.add(j)
        


        self.flipOneDotThreeToZero()