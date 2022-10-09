#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
import itertools
from typing import List



class Solution:
    def subset_sum(self,sum_needed,n,wt):
        dp = [[-1 for _ in range(sum_needed+1)] for _ in range(n+1)]
        for i in range(sum_needed+1):
            dp[0][i]= False
        for i in range(n+1):
            dp[i][0]=True
        for i, j in itertools.product(range(1,n+1), range(1,sum_needed+1)):
            dp[i][j] = dp[i-1][j] if j < wt[i-1] else dp[i-1][j] or dp[i-1][j-wt[i-1]]
        return dp[n][sum_needed]

             
        
    def canPartition(self,arr:List[int]) -> bool:
        sum_arr = sum(arr)
        if int(sum_arr/2)!=sum_arr/2 or sum_arr%2==1:
            return False
        if int(sum_arr/2) in arr:
            return True
        return self.subset_sum(int(sum_arr/2),len(arr),arr)

        

    
if __name__ == '__main__':
    print(Solution().canPartition([1,2,5,2]))
        
        
        
# @lc code=end

