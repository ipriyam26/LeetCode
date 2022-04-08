import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=997 lang=java
 *
 * [997] Find the Town Judge
 */

// @lc code=start
class Solution {
    public int findJudge(int n, int[][] trust) {

       int[] trusting = new int[n+1];
       int[] trusted = new int[n+1];
      for (int[] relation : trust) {
          trusting[relation[0]]++;
          trusted[relation[1]]++;
      }

      for (int i = 1; i < trusted.length; i++) {
          if(trusted[i]==n-1 && trusting[i]==0){    
return i;
          }
      }
      return -1;
    }

}
// @lc code=end

