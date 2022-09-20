#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List
import heapq



class Solution:
    
    
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        counts = Counter(nums)

        heap = []
        for key in counts:
            heapq.heappush(heap, (counts[key], (-1 *key)))

        output = []
        while heap:
            count, val = heapq.heappop(heap)
            val *= -1

            output.extend(val for _ in range(count))
        return output	
        

        
# @lc code=end

