import java.util.Stack;

/*
 * @lc app=leetcode id=1475 lang=java
 *
 * [1475] Final Prices With a Special Discount in a Shop
 */

// @lc code=start
class Solution {
    public int[] finalPrices(int[] prices) {
        
        for(int i=0;i<prices.length-1;i++){
             for(int j=i+1;j<prices.length;j++){
            if(prices[j]<=prices[i]){
                prices[i]-=prices[j];
                break;
            }
        }
        }
        
        return prices;
    }
}
// @lc code=end
