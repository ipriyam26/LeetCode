#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List
import heapq

class Solution:
    
    def make_frequency_map(self,nums: List[int]):
        hash = {}
        for num in nums:
            if num in hash:
                hash[num]+=1
            else:
                hash[num]=1
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
# @lc code=end

