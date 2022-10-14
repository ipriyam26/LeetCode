/*
 * @lc app=leetcode id=1143 lang=cpp
 *
 * [1143] Longest Common Subsequence
 */
#include <iostream>
#include <algorithm>
// @lc code=start
using namespace std;
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.length();
        int m = text2.length();
        int dp[n+1][m+1];
        for (int i = 0; i < n+1; i++)
        {
            for (int j = 0; j < m+1; j++)
            {
                dp[i][j]=0;
            }
            
        }
        
        // cout<<n<<" "<<m<<endl;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if(text1[i-1]==text2[j-1]){
                    dp[i][j] = 1+dp[i-1][j-1];
                }
                else{
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }

                
            }
        }
        // cout<<dp[n][m];
        return dp[n][m];
        
         
    }
};
// @lc code=end

