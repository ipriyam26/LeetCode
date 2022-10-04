#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        i,j = 0,0
        one = 0
        while j <len(nums):
            if nums[j]==1:
                one+=1
            if one<goal:
                j+=1
            if one==goal:
                count+=1
                j+=1
            elif(one>goal):
                while one>goal and i<j:
                    if nums[i]==1:
                        one-=1
                    i+=1
                if one==goal:
                    count+=1
            # j+=1
        # print()
        return count

if __name__ == '__main__':
    res = Solution()
    print(res.numSubarraysWithSum(nums=[1,0,1,0,1],goal=2))
    
                    
                
            
# @lc code=end

