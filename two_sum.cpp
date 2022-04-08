#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();

        int high = n-1;
        int low = 0;
        int mid;
        while(high>low){
            mid = (high+low)/2;
            if(nums[mid]> target){
                if(nums[mid+1]<target){
                    return mid;
                }
                high = mid-1; 
            }else if (nums[mid]<target)
            {
                if(nums[mid+1]>target){
                    return mid;
                }
                low = mid+1;
            }
            else{
                return mid;
            }
        }
        
    }
};
