from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # start,end = 0,0

        arr_sum  = nums[0]
        max_sum  = arr_sum
        p = 0

        for num in nums[1:]:
            p = num + arr_sum
            arr_sum = max(p, num)
            max_sum = max(arr_sum,max_sum)
        return max_sum

    
    
print(Solution().maxSubArray( [-2,1,-3,4,-1,2,1,-5,4]))