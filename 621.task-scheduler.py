#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from heapq import heappop, heappush, heapify
from typing import Dict, List
from collections import Counter

class Solution:
    
    
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        m = len(tasks)
        
        counter_all = Counter(tasks)
        
        counter = sorted(list(counter_all.values()),reverse=True)
        
        maximum = counter[0]-1
        
        maximum_spaces = maximum*n
        

        for item in counter[1:]:
            maximum_spaces-= min(maximum,item)

        return m + max(0,maximum_spaces)
            
            

# @lc code=end

