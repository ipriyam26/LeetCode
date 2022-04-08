import java.util.ArrayList;
import java.util.HashMap;

/*
 * @lc app=leetcode id=207 lang=java
 *
 * [207] Course Schedule
 */

// @lc code=start
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
       HashMap<Integer,ArrayList<Integer>> adj = new HashMap<Integer,ArrayList<Integer>>(); 
       for (int i = 0; i < numCourses; i++) {
           adj.put(i, new ArrayList<Integer>());
       }
       for (int[] prerequisite : prerequisites) {
           adj.put(prerequisite[0], )
       }
       
    }
}
// @lc code=end

