/*
 * @lc app=leetcode id=238 lang=java
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
class Solution {
    public int[] productExceptSelf(int[] nums) {
       int product = 1;
       int productIgnoringZeros = 1;
       int zeroCount = 0;
       for (int i : nums) {
        product*=i;
        if(i!=0){
            productIgnoringZeros*=i;
        }
        else{
            zeroCount++;
        }
       } 
       int[] result = new int[nums.length];

       for (int i = 0; i < result.length; i++) {
        if(nums[i]==0 && zeroCount==1){
            result[i] = productIgnoringZeros;
        }
        else{
            result[i] = product/nums[i];
        }
       }

       return result;

    }
}
// @lc code=end

