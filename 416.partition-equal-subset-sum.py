#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from typing import List



class Solution:
    def is_subset(self,N, sum,nums,total_sum):
        if (N==0):
            return sum == total_sum/2
        if sum - nums[N-1] <total_sum/2:
            return self.is_subset(N-1,sum,nums,total_sum=total_sum)
        else:
            return self.is_subset(N-1,sum,nums,total_sum=total_sum) or self.is_subset(N-1,sum-nums[N-1],total_sum=total_sum)
        
    def canPartition(self, nums: List[int]) -> bool:
        
        total_sum = sum(nums)
        if total_sum %2==1:
            return False
        else:
            return self.is_subset(len(nums),0,nums,total_sum=total_sum)
        
        
        
# @lc code=end

