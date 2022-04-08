
/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */
import java.util.*;

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        int i = 0;
        Map<Character,Character> map = new HashMap<Character,Character>();
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
        while (i < s.length()) {
            char ch = s.charAt(i);
            if (map.containsKey(ch)) {
                stack.push(ch);
            } else {
                if(stack.isEmpty()){
                    return false;
                }
                char ans = map.get(stack.peek());
                if (ans == ch) {
                    stack.pop();
                } else {
                    return false;
                }
            }

            // stack.push(s.charAt(i));
            i++;
        }

        if (stack.isEmpty()) {

            return true;
        }
        return true;
    }
}
// @lc code=end
