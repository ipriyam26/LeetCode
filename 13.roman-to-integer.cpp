/*
 * @lc app=leetcode id=13 lang=cpp
 *
 * [13] Roman to Integer
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int romanToInt(string s)
    {
        int sum = 0;
        int len = s.length();
        // int k = romanToInt(s);

        unordered_map<char, int> roman{
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
            // {'IV', 4},
            // {'IX', 9},
            // {'XL', 40},
            // {'XC', 90},
            // {'CD', 400},
            // {'CM', 900},
        };
        // return k;
        int L;
        int R;
        // for (int i = len-1; i >= 0; i--)
        // {
        //     sum+=roman[s[i]];
        // }
        // string k ="Priyam"  ;
        // cout<<k[0]<<" "<<k[5];
        // sum=0;
        for (int i = 0; i < len; i++)
        {
            L = roman[s[i]];
            if (i != len-1)
            {
                R = roman[s[i + 1]];
                if (R > L)
                {
                    sum += (R-L);
                    i++;
                }
                else
                {
                    sum += L;
                }
            }else{

            sum += L;
            }
        }
        return sum;
    }
};
// @lc code=end
