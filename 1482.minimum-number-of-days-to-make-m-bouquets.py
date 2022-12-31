#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
from typing import List


class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def condition(day: int):
            flowers,    bouguets = 0,0
            for bloom in bloomDay:
                if bloom>day:
                    flowers=0
                else:
                    bouguets+=(flowers+1)//k
                    flowers = (flowers+1)%k
        
            return bouguets>=m
        
        if m*k>len(bloomDay):
            return -1
        start = min(bloomDay)
        end = max(bloomDay) 
        while start<end:
            mid = (start+end)//2
            if condition(mid):
                end = mid
            else:
                start = mid+1
        return start
                
         
# @lc code=end

