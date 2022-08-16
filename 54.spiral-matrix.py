#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        X = len(matrix[0])
        Y = len(matrix)
        ans = []
        x,y=0,0
        while True:
            while x<X:
                ans.append(matrix[y][x])
                x+=1
            y+=1
            x-=1
            X-=1
            while y<Y:
                ans.append(matrix[y][x])
                y+=1
            Y-=1
            y-=1
            x-=1
            while x>=0:
                ans.append(matrix[y][x])
                x-=1
            x+=1
            y-=1
            
        
# @lc code=end

