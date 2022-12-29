#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        
        start = 0
        end=n-1
        while start<end:
            mid = start+(end-start)//2
            if nums[mid]<nums[mid+1]:start=mid+1
            else: end=mid
        return start
        
# @lc code=end

