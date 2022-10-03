#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j=0,0
        max_count = 0
        zero_count=[]
        
        while j < len(nums):
            if(nums[j]==0):
                zero_count.append(j)
                
            if (len(zero_count) <= k) and (max_count < j - i + 1):
                max_count= j-i+1
            elif(len(zero_count) >k):
                i = zero_count[0]+1
                zero_count.pop(0)
            j+=1
        
        return max_count

if __name__=='__main__':
    arr = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k =3
    print(Solution().longestOnes(arr,k))
        
# @lc code=end

