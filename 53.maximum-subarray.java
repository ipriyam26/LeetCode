/*
 * @lc app=leetcode id=53 lang=java
 *
 * [53] Maximum Subarray
 */

// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {

       int   sum=nums[0]; 
       int maxSum = sum;
       int p;
       for (int i = 1; i < nums.length; i++) {
           
        
        p= nums[i]+sum;
        sum = p>nums[i]?p:nums[i];
        maxSum = Math.max(maxSum, sum);

       }
       return maxSum;

    }
}
// @lc code=end

