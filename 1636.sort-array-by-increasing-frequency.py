#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
from dataclasses import dataclass
from typing import List
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
    
    
    def frequencySort(self, nums: List[int]) -> List[int]:
        

        
# @lc code=end

