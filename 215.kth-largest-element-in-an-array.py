#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap,num)
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        return heapq.heappop(minHeap)
        
# @lc code=end

