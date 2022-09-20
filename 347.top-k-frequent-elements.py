#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List
import heapq

class Pair:
        def __init__(self,count,value) -> None:
            self.count = count
            self.value = value
        def __lt__(self,other):
            if self.count<other.count:
                return True
            elif self.count>other.count:
                return False
            else:
                return self.value<other.value
class Solution:
    
    def make_frequency_map(self,nums: List[int]):
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num]=1
        return hash_map
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = self.make_frequency_map(nums)
        ans:List[Pair] = []
        for key,value in frequency_count.items():
            heapq.heappush(ans,Pair(count=value,value=key))
            if len(ans)>k:
                heapq.heappop(ans)
        result = []
        for left_overs in ans:
            result.insert(0,left_overs.value)
        return result
            

        
# @lc code=end

