#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
from typing import List
import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        simple_arr = [abs(element-k) for element in arr]
        max_heap = []
        for element in simple_arr:
            heapq.heappush(max_heap,element)
            if(len(max_heap)>k):
                heapq.heappop(max_heap)
        ans = []
        while max_heap:
            ans.append(heapq.heappop(max_heap)+x)
        
        
        
        
        
        
# @lc code=end

