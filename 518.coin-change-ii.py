#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
import itertools
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return 1 if amount == 0 else self.subset_sum(amount,len(coins),coins)
        
    def subset_sum(self,sum_needed,n,wt):
        dp= [[0 for _ in range(sum_needed+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=1

        for i, j in itertools.product(range(1,n+1), range(1,sum_needed+1)):
            dp[i][j] = dp[i-1][j] if j < wt[i-1] else dp[i-1][j] + dp[i][j-wt[i-1]]
            
        return dp[i][j]
        
# @lc code=end

