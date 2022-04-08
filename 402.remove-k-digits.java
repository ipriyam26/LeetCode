import java.util.Stack;

/*
 * @lc app=leetcode id=402 lang=java
 *
 * [402] Remove K Digits
 */

// @lc code=start
class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> holder = new Stack<Character>();
        char[] number = num.toCharArray();
        k++;
        holder.push(number[0]);
        for (char c : number) {
            if(holder.peek()>=c){
              holder.pop();
              k--;
              if (k==0) {
                  break;
              }
            }
            holder.push(c);
        }
String numb = "";
        while (!holder.isEmpty()) {
           numb = holder.pop() +numb;
        }
        int i=0;
        while(numb.charAt(i)==0){
i++;
        }
        return numb;
        
    }
}
// @lc code=end

