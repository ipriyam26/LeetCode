#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        current_max = min(height[i], height[j]) * (j - i)
        start_left = True
        while j>i:
            #lets try to find a value on the left that is greater than current height
            current_max = max(
                current_max,
                min(height[i], height[j]) * (j - i)
            )
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
                
        return current_max

# if __name__=="__main__":
#     arr = [2,3,10,5,7,8,9]
#     print(Solution().maxArea(arr))
        
# @lc code=end
