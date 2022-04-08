import java.util.Stack;

/*
 * @lc app=leetcode id=150 lang=java
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<Integer>();
        for (String token : tokens) {

            if (token.equals("+")) {
                int last = stack.pop();
                int first = stack.pop();
                stack.push(last + first);
            } else if (token.equals("-")) {

                int last = stack.pop();
                int first = stack.pop();
                stack.push(first - last);

            } else if (token.equals("*"))

            {

                int last = stack.pop();
                int first = stack.pop();
                stack.push(first * last);
            } 
            else if(token.equals("/"))
            {
                int last = stack.pop();
                int first = stack.pop();
                stack.push(first / last);
            }
            else{
                int a = Integer.parseInt(token);
                stack.push(a);
            }
        }

        return stack.pop();
    }
}
// @lc code=end
