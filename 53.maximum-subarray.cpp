/*
 * @lc app=leetcode id=53 lang=cpp
 *
 * [53] Maximum Subarray
 */

// @lc code=start
#include <bits/stdc++.h>
class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        int sum=nums[0],maxSum=nums[0],p;
        for (int i = 1; i < nums.size(); i++)
        {
            p = sum+nums[i];
            sum = p>nums[i]?p:nums[i];
            if(sum>maxSum){
                maxSum = sum;
            }
        }
        return maxSum;
        
    }
};
// @lc code=end

