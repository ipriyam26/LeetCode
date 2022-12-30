#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
from typing import List


class Solution:

   
    def search(self, nums: List[int], target: int) -> int:
            # If the length of the given array list is 1, then check the first element and return accordingly
        if len(nums)==1:
            return nums[0] == target
        left=0
        right=len(nums)-1
        # binary search
        while (left<=right):

            # shifting to remove duplicate elements
            while left<right and nums[left] == nums[left+1]:
                left+=1
            while left<right and nums[right] == nums[right-1]:
                right-=1

            # step 1 calculate the mid    
            mid=(left+right)//2

            #step 2
            if nums[mid]==target:
                return True

            elif nums[left]<=nums[mid]:
                if nums[mid]>=target and nums[left]<=target:
                    right=mid-1
                else:
                    left=mid+1

            elif target>=nums[mid] and target<=nums[right]:
                left=mid+1
            else:
                right=mid-1

        # step 5
        return False


        
# @lc code=end

