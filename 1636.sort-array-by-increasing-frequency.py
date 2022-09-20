#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
from dataclasses import dataclass
from typing import Dict, List
import heapq

@dataclass
class Pair:
   count:int
   value:int
   def __lt__(self,other):
       if self.count<other.count:
           return True
       elif self.count>other.count:
           return False
       else:
           return self.count>other.count 

class Solution:
    
    def make_frequency_map(self,nums: List[int])-> Dict[int,int]:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num]=1
        return hash_map
    
    def frequencySort(self, nums: List[int]) -> List[int]:
       frequency_count = self.make_frequency_map(nums)
       ans = []
       for value,count in frequency_count.items():
           heapq.heappush(ans,Pair(count=count,value=value))
       result = []
       while ans:
          pooped:Pair = heapq.heappop(ans)
          result.extend(pooped.value for _ in range(pooped.count))
       return result
        

        
# @lc code=end

