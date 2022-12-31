#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List
import math

class Solution:


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        n = max(piles)
        k,r = n,n
        while l<=r:
            mid = l + (r-l)//2
            hours = sum(math.ceil(p/mid) for p in piles)
            if hours<=h:
                k = min(mid,k)
                r = mid-1

            else:
                l = mid+1
        return k 
             
# @lc code=end

