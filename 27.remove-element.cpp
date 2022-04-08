/*
 * @lc app=leetcode id=27 lang=cpp
 *
 * [27] Remove Element
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int result = 0;
        if(nums.size() == 0){
            return result;
        }
        for(int i = 0;i < nums.size();i++){
            if(nums[i] != val){
                nums[result] = nums[i];
                result++;
            }
        }
        return result;
    }
};
// @lc code=end

