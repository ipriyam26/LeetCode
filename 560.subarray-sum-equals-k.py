#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i,j=0,0
        max_length  = 0
        value = 0
        while j<len(nums):
            value+=nums[j]
            if(value<k):
                continue
            elif(value==k):
                if i-j+1>max_length:
                    max_length = i-j+1
            else:
                while(value>k):
                    i+=1
                    value-=nums[i]
                    
            j+=1
                
            
        
# @lc code=end

