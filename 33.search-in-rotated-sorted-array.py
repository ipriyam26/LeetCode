#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    
    def find_piviot(self,nums: List[int]):
        start = 0
        end = len(nums)-1
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
   
                
    def binary_search(self, nums: List[int], target: int,start,end) -> int:


        while start<=end:
            mid = start + (end - start)//2
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end= mid-1
            else:
                return mid
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        piviot = self.find_piviot(nums=nums)
        n = len(nums)
        if piviot==-1:
            return self.binary_search(nums,target,0,n-1)
        if nums[piviot]==target:
            return piviot
        return (
            self.binary_search(nums, target, 0, piviot)
            if target >= nums[0]
            else self.binary_search(
                nums, target=target, start=piviot + 1, end=n - 1
            )
        )

        

        
# @lc code=end

