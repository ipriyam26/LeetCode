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
            return self.value>other.value
            
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.reverse()
        simple_arr = [self.Pair(abs(element-x)*-1,element) for element in arr]
        max_heap = []
        for element in simple_arr:
            heapq.heappush(max_heap,element)
            if(len(max_heap)>k):
                print(heapq.heappop(max_heap).index)
        ans = []
        while max_heap:
            ans.insert(0,heapq.heappop(max_heap).index)

        return ans
        
        
        
        
# @lc code=end

