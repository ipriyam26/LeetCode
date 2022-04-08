/*
 * @lc app=leetcode id=66 lang=cpp
 *
 * [66] Plus One
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> plusOne(vector<int> &digits)
    {
        int last = digits.size() - 1;
        int lastDigit = digits[last];
        if (lastDigit == 9)
        {
            for (; last >= 0; last--)
            {
                if (digits[last] != 9)
                {
                    digits[last]++;
                    return digits;
                }
                else
                {
                    digits[last] = 0;
                }
            }
            digits[0] = 1;
            digits.push_back(0);
            return digits;
        }

        digits[last]++;
        return digits;
    }
};
// @lc code=end
