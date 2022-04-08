/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];
for(int i =1;i<strs.length;i++)
            {while (true) {
                if(strs[i].startsWith(prefix)){
                    break;
                }else{
                    if(prefix.isEmpty()){
                        return prefix;
                    }
                    prefix =prefix.substring(0, prefix.length()-1);
                }
            }}

        return prefix;
    }
}
// @lc code=end

