#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
import heapq
from typing import List


class Solution:
        
    def make_frequency_map(self,nums: List[int]):
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num]=1
        return hash_map
    
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq_list = self.make_frequency_map(hand)
        if(len(hand)%groupSize!=0):
            return False
        holder = []
        
        for value,count in freq_list.items():
            heapq.heappush(holder,(value,count))
        
        
        
# @lc code=end

