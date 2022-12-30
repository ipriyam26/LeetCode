#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    
    
    
    
    def find_piviot(self,nums: List[int],start: int ,end:int):

        while start<=end:
            mid = start + (end - start)//2
            
            if mid<end and nums[mid]>nums[mid+1]:
                return mid
            elif mid>start and nums[mid]<nums[mid-1]:
                return mid-1
            
            
            if nums[mid]<=nums[start]:
                end = mid-1
            else:
                start=mid+1
        return -1
   
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        end = n-1
        return nums[(self.find_piviot(nums,0,end)+1)%n]

# @lc code=end

