#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=start
from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(value:int) -> bool: 
            res = sum((num-1)//value + 1 for num in nums)
            return res<=threshold
        left, right = 1, max(nums)
        while left < right: 
            mid = left + (right - left) // 2 
            if condition(mid): 
                right = mid 
            else: 
                left = mid + 1 
        return left
        
# @lc code=end

