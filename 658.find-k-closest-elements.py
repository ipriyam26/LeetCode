#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
from typing import List
import heapq

class Solution:
    
    class Pair:
        def __init__(self,value,index) -> None:
            self.value=value
            self.index = index
        def __lt__(self,other):
            return self.value<other.value
            
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        simple_arr = [self.Pair(abs(element-x),i) for i,element in enumerate(arr)]
        max_heap = []
        for element in simple_arr:
            heapq.heappush(max_heap,element)
            if(len(max_heap)>k):
                heapq.heappop(max_heap)
        ans = []
        while max_heap:
            ans.insert(0,heapq.heappop(max_heap).value)
        
        return ans
        
        
        
        
# @lc code=end

