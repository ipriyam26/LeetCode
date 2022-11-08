#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max( prices[i+1]-prices[i],0 ) for i in range(len(prices)-1))
        
# @lc code=end

