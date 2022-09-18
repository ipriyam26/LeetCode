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
        minHeap:heapq = heapq()
        for num in nums:
            minHeap.heappush(num)
            if len(minHeap)>k:
                minHeap.heappop()
        return minHeap.heappushpop()
        
# @lc code=end

