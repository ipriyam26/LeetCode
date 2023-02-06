/*
 * @lc app=leetcode id=121 lang=java
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start


class Solution {
    public int maxProfit(int[] prices) {
       int currentMax = 0;
       int profit=0;
    for (int i = prices.length-1; i >=0; i--) {
        profit = Math.max(currentMax-prices[i],profit  );
        currentMax = Math.max(currentMax,prices[i]);
    }
    return profit;
    }
}
// @lc code=end

