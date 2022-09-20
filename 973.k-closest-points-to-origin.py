#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [] 
        for dimensions in points:
            x,y = dimensions
            heapq.heappush(distance,(-1*(x*x+y*y)**0.5,dimensions))
            if len(distance)>k:
                heapq.heappop(distance)
        result = []
        while distance:
            pooped = heapq.heappop(distance)[1]
            result.index(0,pooped)
        return result
            
            
            
           
# @lc code=end

