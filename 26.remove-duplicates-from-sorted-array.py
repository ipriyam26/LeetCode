#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=-101
        p=0
        i =0
        while i<len(nums):
            if k!=nums[i]:
                k=nums[i]
                p+=1
            else:
                nums.remove(k)
                nums.append(101)
            i+=1    
        return p
# @lc code=end

