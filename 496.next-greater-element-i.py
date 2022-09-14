#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from typing import List


class Solution:
    
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngr = self.find_NGR(nums2)
        return [ ngr[nums2.index(num)] for num in nums1 ]

    def find_NGR(self,arr:List[int])-> List[int]:
        stack = []
        res = []
        i =len(arr)-1
        while i>=0:
            if not stack:
                res.append(-1)
            elif (stack[-1] >arr[i]):
                res.append(stack[-1])
            else:
                while stack and stack[-1]<arr[i]:
                    stack.pop()
                if not stack:
                    res.append(-1)
                else:
                    res.append(stack[-1])
            stack.append(arr[i])
            i-=1
        res.reverse()
        return res
         

        
# @lc code=end

