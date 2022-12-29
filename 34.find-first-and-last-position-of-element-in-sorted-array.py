#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        s,e = -1,-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end= mid-1
            else:
                # this is the first occurence
                if nums[mid-1]!=target:
                    s=mid
                    start=mid+1
                if nums[mid+1]!=target:
                    e=mid
                    end+=mid-1
                if s !=-1 and e!=-1:
                    return [s,e]
        return [s,e]
        
# @lc code=end

