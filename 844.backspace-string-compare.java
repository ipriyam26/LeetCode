import java.util.Stack;

/*
 * @lc app=leetcode id=844 lang=java
 *
 * [844] Backspace String Compare
 */

// @lc code=start
class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> word1 = new Stack<Character>();
        Stack<Character> word2 = new Stack<Character>();
        
        for (int i = 0; i < s.length(); i++) {
            char p = s.charAt(i);
            if (p == '#') {
                try {
                    
                    word1.pop();
                } catch (Exception e) {
                    continue;
                }
                continue;
            }
            word1.push(p);
        }
        for (int i = 0; i < t.length(); i++) {
            char p = t.charAt(i);
            if (p == '#') {
                try {
                    
                    word2.pop();
                } catch (Exception e) {
                    continue;
                }
                continue;
               
            }
            word2.push(p);
        }
        if (word1.size() != word2.size()) {
            return false;
        }
        while (!word1.isEmpty()) {
            if (word1.pop() != word2.pop()) {
                return false;
            }

        }
        return true;

    }
}
// @lc code=end
