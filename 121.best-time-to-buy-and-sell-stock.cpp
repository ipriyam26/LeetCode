/*
 * @lc app=leetcode id=121 lang=cpp
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int max = 0, sum;
        int len = prices.size();
        for (int i = 0; i < len; i++)
        {
            for (int j = i + 1; j < len; j++)
            {
                sum = prices[j] - prices[i];
                if ((sum) > max)
                {
                    max = sum;
                }
            }
        }
        return max;
    }
};
// @lc code=end
