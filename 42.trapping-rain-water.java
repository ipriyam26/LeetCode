import java.util.Arrays;

/*
 * @lc app=leetcode id=42 lang=java
 *
 * [42] Trapping Rain Water
 */

// @lc code=start
class Solution {

    public int[] largestToRight(int[] height){
        int[] result = new  int[height.length];
        int max=0;
        for(int i =0;i<height.length;i++){
            result[i]= max;
            if(height[i]>max){
                max = height[i];
            }
        }
        return result;
    }

    public int[] largestToLeft(int[] height){
        int[] result = new  int[height.length];
        int max=0;
        for(int i =height.length-1;i>=0;i--){
            result[i]= max;
            if(height[i]>max){
                max = height[i];
            }
        }
        return result;
    }

    public int trap(int[] height) {
        // int[] LFR = largest_from_right(height);
        int[] LTR = largestToRight(height);
        int[] LTL = largestToLeft(height);
        System.out.println(Arrays.toString(LTR));
        System.out.println(Arrays.toString(LTL));
        // int[] result = new int[height.length];
        int result=0;
        for(int i=0;i<height.length;i++){
            int value = Math.min(LTR[i], LTL[i]) - height[i];
           if(value>0){
            result+=value;
           }
        }
        return result;
    }
}
// @lc code=end

