/*
 * @lc app=leetcode id=67 lang=cpp
 *
 * [67] Add Binary
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string addBinary(string a, string b)
    {
        string ans = "";
        int lastA = a.length() - 1;
        int lastB = b.length() - 1;
        if(lastA>lastB){
            while (lastB!=lastA)
            {
                b = '0'+b;
                lastB++;
            }
            
        }
        else{
             while (lastB!=lastA)
            {
                a = '0'+a;
                lastA++;
            }
        }
        char carry = '0';

        while (lastA >=0)
        {

            if (a[lastA] == '1' && b[lastB] == '1')
            {
                if (carry == '0')
                {
                    ans = '0' + ans;
                    carry = '1';
                }
                else
                {
                    ans = '1' + ans;
                    carry = '1';
                }
            }
            else if ((a[lastA] == '0' && b[lastB] == '1') )
            {
                if (carry == '0')
                {
                    ans = '1' + ans;
                    carry = '0';
                }
                else
                {
                    ans = '0' + ans;
                    carry = '1';
                }
            }
            else if ( (a[lastA] == '1' && b[lastB] == '0'))
            {
                if (carry == '0')
                {
                    ans = '1' + ans;
                    carry = '0';
                }
                else
                {
                    ans = '0' + ans;
                    carry = '1';
                }
            }
            else
            {
                if (carry == '1')
                {
                    ans = '1' + ans;
                    carry = '0';
                }
                else
                {
                    ans = '0' + ans;
                    carry = '0';
                }
            }

            lastA--;
            lastB--;
        }
        if(carry=='1'){
            ans = '1'+ans;
        }
        return ans;
    }
};
// @lc code=end
