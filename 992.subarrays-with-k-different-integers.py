#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        i,j=0,0
        unique = 0
        latest = {}
        result = 0
        while j <len(nums):
            
            #check if the element is already there in latest map
            if nums[j] not in latest:
                unique+=1
            
            #update the latest position for the current variable
            latest[nums[j]]=j
            

            
            
            #When the number of unique variables increase the number
            #of needed variables
            if unique>k:
                #we are squeezing the window from the back until we are able to remove the element the increased the unique count i.e until we are able to limit the count of unique digits to be within k.
               
               #we iterate ato find any number, whose latest occurrence is about to be removed as that would mean we are removing a distinct integer 
                # while latest[nums[i]]!=i:
                #     i+=1
                
                i += min(latest.values())
                
                #remove the element from the latest map as it is no longer gonna exist and move forward and decrease unique
                latest.pop(nums[i])
                i+=1
                unique-=1
            
             
            # When the number of unique elements matches the amount needed by us    
            if unique==k:
                result+=1
                #We will make a temporary pointer and iterate until we find an element which is about to reach its latest occurrence
                if j==len(nums)-1:
                    break
                result+=min(latest.values())
                # temp = i
                # while latest[nums[temp]]!=temp:
                #     result+=1
                #     temp+=1
                
           
            j+=1
        
        return result
    
if __name__ =='__main__':
    print(Solution().subarraysWithKDistinct(nums=[2,1,1,1,2],k=1))
                    
                        
            
        
# @lc code=end

