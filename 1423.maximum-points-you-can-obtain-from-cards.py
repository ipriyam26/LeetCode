#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i,j=0,0
        if k==len(cardPoints):
            return sum(cardPoints)
        min_k = len(cardPoints)-k
        print("Min k ",min_k)
        result = 0
        min_result = 1000000
        n=1
        while j <len(cardPoints):
            result+=cardPoints[j]
            if n<min_k:
                n+=1
                # j+=1
            else:
                min_result = result
                print(min_result)
                while j<len(cardPoints)-1:
                    
                    result = result-cardPoints[i] +cardPoints[j+1]
                    print(result)
                    min_result = min(result,min_result)
                    j+=1
                    i+=1
            j+=1
        print(min_result)
        return sum(cardPoints)-min_result
                
                
            
            
            
        
            
        
# @lc code=end

