import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=3 lang=java
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0, max = 0;

        HashMap<Character, Integer> dict = new HashMap<Character, Integer>();
        int len = s.length();
        if (len == 0) {
            return 0;
        } 
        // else if (len == 1) {
        //     return 1;
        // }
int j;
        for(i=0, j=0;i<len;i++ )
         {
            char a = s.charAt(i);

            if (dict.containsKey(a)) {
                // doing this max makes it possible for us to be not clear dict each time we find a match
                // move pointer just next to the place where the element has already occured
                j = Math.max(j,dict.get(a)+1);
            } 
            dict.put(a, i);
            max = i-j+1>max?i-j+1:max;



        }
        return max;

    }
   



}
// @lc code=end

