#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counter = Counter()
        odd=0
        counter[0]+=1
        for num in nums:
            if num%2==1:
                odd+=1
            counter[odd]+=1
        # print(counter.keys())
        # print(counter.values())
        # i,j,ans=0,0,0
        j=k
        i=0
        ans=0
        while j<=odd:
            ans+=counter[j]*counter[i]
            j+=1
            i+=1
        return ans
            
            
        

            
# @lc code=end

