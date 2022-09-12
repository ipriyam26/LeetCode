#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = {}
        nums2.reverse()
        for num in nums2:
            if not stack:
                ans[num] = -1
            while stack and num >= stack[-1]:
                stack.pop()
            ans[num] = stack[-1] if stack else -1
            stack.append(num)
        return [ans[n] for n in nums1]
            
            
                
                
            
            
            

            
            
                
            

            

        
# @lc code=end

