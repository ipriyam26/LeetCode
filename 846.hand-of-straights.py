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
        
        while holder:
            buffer = []
            prev = 0

            for _ in range(groupSize):
                try:
                    pooped = heapq.heappop(holder)
                except:
                    return False
                if prev!=0 and prev+1!=pooped[0]:
                    return False
                if pooped[1]>1:
                    buffer.append((pooped[0],pooped[1]-1))
                prev = pooped[0]
            print(holder)
            for item in buffer:
                heapq.heappush(holder,item)

        return True
                
                
        
# @lc code=end

