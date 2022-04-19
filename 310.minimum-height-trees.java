import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/*
 * @lc app=leetcode id=310 lang=java
 *
 * [310] Minimum Height Trees
 */

// @lc code=start
class Solution {

    public ArrayList<ArrayList<Integer>> makeAdjacencyList(int[][] pre, int num) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i < num; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] course : pre) {
            adj.get(course[0]).add(course[1]);
            adj.get(course[1]).add(course[0]);

        }

        return adj;
    }

    public List<Integer> findMinHeightTrees(int n, int[][] edges) {

      
    }
}
// @lc code=end
