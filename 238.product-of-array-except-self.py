#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List
import functools
import operator

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product_without_0 =1
        contains_0 = nums.count(0)
        if contains_0>=2:
            return [0]*len(nums)
        elif contains_0==1:
            return self._extracted_from_productExceptSelf_7(nums)
        else:
            prod = int(functools.reduce(operator.mul,nums))
            return [prod//num for num in nums]

    # TODO Rename this here and in `productExceptSelf`
    def _extracted_from_productExceptSelf_7(self, nums):
        temp_arr = nums.copy()
        temp_arr.remove(0)
        prod = int(functools.reduce(operator.mul,temp_arr))
        res = []
        for num in nums:
            if num==0:
                res.append(prod)
            else:
                res.append(0)
        return res
            
            
            

        
# @lc code=end

