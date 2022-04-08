/*
 * @lc app=leetcode id=26 lang=java
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
import java.util.Arrays;

class Solution {
    public int removeDuplicates(int[] nums) {
        int k =-101;
        int p =0;
        for (int i = 0; i < nums.length; i++) {
                if(k!=nums[i]){
                    k=nums[i];
                    p++;
                }else{
                    nums[i]=101;
                }

        }
        Arrays.sort(nums);
return p;
    }
}
// @lc code=end

