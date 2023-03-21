#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        
        out = []
        
        for i,element in enumerate(nums):
            
            while dq and nums[dq[-1]]<element:
                dq.pop()
            
            
            dq.append(i)
            
            if dq[0]==i-k:
                dq.popleft()
            
            if i>=k-1:
                out.append(nums[dq[0]])
                
        return out
            
        
# @lc code=end

