/*
 * @lc app=leetcode id=493 lang=java
 *
 * [493] Reverse Pairs
 */

// @lc code=start
class Solution {

    public int merger(int[] nums,int l,int r){
if (l>=r){
    return 0;
}
int m = l + ((r-l)>>1);
int res = merger(nums, l, m) + merger(nums, m+1, r);

// int[] merge = 
int i=l,j=m+1,k=0,p=m+1;
int[] merge = new int[r-l+1];

while (i <= m) {
    while (p <= r && (long)nums[i] > (long)2* nums[p]) p++;
    res += p - (m + 1);
            
    while (j <= r && nums[i] >= nums[j]) merge[k++] = nums[j++];
    merge[k++] = nums[i++];
}
while (j <= r) merge[k++] = nums[j++];
        
System.arraycopy(merge, 0, nums, l, merge.length);
    
return res;


    }
    public int reversePairs(int[] nums) {
     return merger(nums, 0, nums.length-1);   
    }
}
// @lc code=end

