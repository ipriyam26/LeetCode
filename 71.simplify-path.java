import java.util.Stack;

/*
 * @lc app=leetcode id=71 lang=java
 *
 * [71] Simplify Path
 */

// @lc code=start
class Solution {
    public String simplifyPath(String path) {
       
        // Stack<Character> stack = new Stack<Character>();
        String final_path ="";
        String temp ="";
        for (int i = 0; i < path.length(); i++) {
            char a = path.charAt(i);
            if(a!='/'){
                temp+=a;
            }
            else{
                if((!temp.equals("..") || !temp.equals(".")) && !temp.isEmpty() ){
                    final_path= final_path+'/'+temp;
                
                }
                temp="";
            }
        }
        return final_path;

    }
}
// @lc code=end

