import java.util.Arrays;
import java.util.Stack;

/*
 * @lc app=leetcode id=84 lang=java
 *
 * [84] Largest Rectangle in Histogram
 */

// @lc code=start
class Solution {

    class Element{
        int value;
        int index;

        Element(int value,int index){
            this.value = value;
            this.index = index;
        }
    }

    public int[] nearestLowerLeft(int[] heights){
        Stack<Element> stk = new Stack<Element>();
        int[] res = new int[heights.length];
        for(int i=0;i<heights.length;i++){
            if (stk.empty()){
               res[i]=-1; 
            }
            else if(stk.peek().value<heights[i]){
                res[i] = stk.peek().index;
            }
            else{
                while (!stk.empty() && stk.peek().value>=heights[i]){
                    stk.pop();
                }
                if(stk.isEmpty()){
                    res[i] = -1;
                }
                else{
                    res[i] = stk.peek().index;
                }

            }
            stk.add(new Element(heights[i], i));
        }

        return res;

    }
    public int[] nearestLowerRight(int[] heights){
        Stack<Element> stk = new Stack<Element>();
        int[] res = new int[heights.length];
        for(int i=heights.length-1;i>=0;i--){
            if (stk.empty()){
               res[i]=heights.length; 
            }
            else if(stk.peek().value<heights[i]){
                res[i] = stk.peek().index;
            }
            else{
                while (!stk.empty() && stk.peek().value>=heights[i]){
                    stk.pop();
                }
                if(stk.isEmpty()){
                    res[i] = heights.length;
                }
                else{
                    res[i] = stk.peek().index;
                }

            }
            stk.add(new Element(heights[i], i));
        }

        return res;

    }

    public int largestRectangleArea(int[] heights) {
        // System.out.println(Arrays.toString(nearestLowerLeft(heights)));
        // System.out.println(Arrays.toString(nearestLowerRight(heights)));
        int[] NLL = nearestLowerLeft(heights);
        int[] NLR = nearestLowerRight(heights);
        int[] result = new int[heights.length];
        int ans=0;
        for(int i =0;i<heights.length;i++){
            result[i] = Math.abs(NLR[i]-NLL[i]-1)*heights[i];
            if (result[i]>ans){
                ans = result[i];
            }
        }

        return ans;
        
    }
}
// @lc code=end

