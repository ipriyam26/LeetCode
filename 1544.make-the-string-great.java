import java.util.Stack;

/*
 * @lc app=leetcode id=1544 lang=java
 *
 * [1544] Make The String Great
 */

// @lc code=start
class Solution {
    public String makeGood(String s) {
        // Stack<Character> stack = new Stack<Character>();
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < s.length() ; i++) {
            char an = s.charAt(i);
            if (str.length()==0) {
                str.append(an);
                // stack.push(an);

            } else {
                char last = str.charAt(str.length()-1);
                if (Character.toLowerCase(an) == Character.toLowerCase(last) && an != last) {
                    str.deleteCharAt(str.length()-1);
                } else {
                    str.append(an);
                    // stack.push(an);
                }
            }
        
        }
        return str.toString();
        
    }
}
// @lc code=end
