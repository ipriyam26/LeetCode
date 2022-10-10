#
# @lc app=leetcode id=2035 lang=python3
#
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference
#

# @lc code=start
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        #~ Main idea
        # The minimum difference between two subarray is ideally 0
        # , to find zero we need the two subarrays to be half, so try to find half
        # if we find half then min diff is zero else we find the min diff from half.
        sum_of_array = sum(nums)
        if(sum_of_array==0):return 0
        to_be_found=sum_of_array//2
        self.dp= [[None for _ in range(to_be_found+1)] for _ in range(len(nums)+1)]
        diff = self.findHalf(nums=nums,target=to_be_found,n=len(nums))
        
        found_half = to_be_found-diff
        other_half = sum_of_array-found_half
        return other_half-found_half
        
    def findHalf(self,nums: List[int],target:int,n:int)->int:

        if target==0:
            return 0
        if n==0:
            return target
        if self.dp[n][target]:
            return self.dp[n][target]
        
        if target<nums[n-1]:
            self.dp[n][target]= self.findHalf(nums,target,n-1)
        else:
            self.dp[n][target]=min(self.findHalf(nums,target-nums[n-1],n-1),self.findHalf(nums,target,n-1))
        return self.dp[n][target]

if __name__ == "__main__":
    arr = []
        
        
        
        
# @lc code=end

