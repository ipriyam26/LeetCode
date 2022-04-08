/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {
    string n = to_string(x);
    int len = n.length();
    string left = len%2==0?n.substr(0,len/2):n.substr(0,len/2+1);
    string right = n.substr(len/2);
    reverse(right.begin(),right.end());
    // cout<<left<<" "<<right;
    if(right==left){
return true;
    }
    else{
return false;
    }
    // u s i n g
    // 0 1 2 3 4
    
    }
};
// @lc code=end

