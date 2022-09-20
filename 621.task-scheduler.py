#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from heapq import heappop, heappush
from typing import Dict, List


class Solution:
    
    def make_frequency_map(self,nums: List[str]):
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num]+=1
            else:
                hash_map[num]=1
        return hash_map
    
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq:Dict[str,int] = self.make_frequency_map(tasks)
        holder = []
        print(freq)
        for item,count in freq.items():
            heappush(holder,(0,item,count))
        time=0
        while holder:
            time+=1
            pooped = heappop(holder)
            print(pooped)
            time = max(time, pooped[0])
            if count<=1:
                continue
            heappush(holder,(time+n,pooped[1],pooped[2]-1))
        return time
                
            
        

        
# @lc code=end

