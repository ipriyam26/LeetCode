import java.util.Stack;

/*
 * @lc app=leetcode id=682 lang=java
 *
 * [682] Baseball Game
 */

// @lc code=start
class Solution {
    public int calPoints(String[] ops) {
        Stack<Integer> stack = new Stack<Integer>();
        for (int i=0;i<ops.length;i++) {
           String element = ops[i];
            try {
                int k = Integer.parseInt(element);
                stack.push(k);
                // System.out.println(stack.size());
            } catch (Exception e) {
               if(element.equals("+")){
                   int n1 = stack.pop();
                   int n2 = stack.peek();
                   int n = n1+n2;
                   stack.push(n1);
                   stack.push(n);
               }
               else if(element.equals("D")){
                   int n = stack.peek()*2;
                   stack.push(n);
               }
               else{
                   stack.pop();
               }
            }
        }
        int ans=0;
        while(!stack.isEmpty()){
ans = ans+stack.pop();
        }
        return ans;

    }
}
// @lc code=end

