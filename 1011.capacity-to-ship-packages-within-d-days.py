#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from typing import List


class Solution:



    def shipWithinDays(self, weights: List[int], days: int) -> int:
                
        def condition(value) -> bool: 
            
            cut_off = 0
            day=1
            for weight in weights:
                if cut_off+weight<=value:
                    cut_off+=weight
                else:
                    cut_off=weight
                    day+=1
            return day<=days
                    
            
            
        left, right = max(weights), sum(weights)
        while left < right: 
            mid = left + (right - left) // 2 
            if condition(mid): 
                right = mid 
            else: 
                left = mid + 1 
        return left
        
# @lc code=end

