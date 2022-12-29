#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    
    
    
    def find_position_to_insert(self, nums: List[int], target: int) -> int:
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
    
    def search_exist(self, nums: List[int], target: int) -> int:
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
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if self.search_exist(nums,target) ==-1:
            return [-1,-1]
        
        # now that we are sure that the number exists
        
        # we can the correct place to insert target - 0.1 ( i.e we find try to index of the first occurrence of the letter)
        
        # any number slightly smaller than target would be inserted at the first occurence of target
        
        start = self.find_position_to_insert(nums=nums,target=target-0.1)
        
        # we do just the opposite and try to find a number that slightly larger than the target and get correct place to insert it
        
        # now remember that the place to insert a number slightly greater that target will be last occurence of target + 1 (i.e just after the target) so we subtract 1 to get last occurence of target   
        end = self.find_position_to_insert(nums=nums,target=target+0.1) - 1
        return [start,end]

        
# @lc code=end

