#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List


class Solution:
    

    
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end= mid-1
            else:
                return mid
        return -1
            
        
        
# @lc code=end

