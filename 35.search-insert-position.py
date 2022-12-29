#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:

    
            
    def searchInsert(self, nums: List[int], target: int) -> int:
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
        return end + 1
        
# @lc code=end

