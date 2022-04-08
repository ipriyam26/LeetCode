import java.util.ArrayList;

/*
 * @lc app=leetcode id=227 lang=java
 *
 * [227] Basic Calculator II
 */

// @lc code=start
class Solution {
    public int calculate(String s) {


    //   char[] ans = s.toCharArray();
    // ans = s.toCharArray();
      char[] order = "/*+-".toCharArray();
      for (char c : order) {
          int i=0;
          while (i<s.length()) {
              if(s.charAt(i)==c){

int first = Integer.parseInt( s.charAt(i-1));
int last = Integer.parseInt(s.charAt(i+1));
              }
          }
      }
    }
}
// @lc code=end

