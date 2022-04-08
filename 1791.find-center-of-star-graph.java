/*
 * @lc app=leetcode id=1791 lang=java
 *
 * [1791] Find Center of Star Graph
 */

// @lc code=start
class Solution {
    public int findCenter(int[][] edges) {
      // we get two elements in each sub array
      // whatever element matches the second sub array that is the center
      if(edges[0][0]==edges[1][0]|| edges[0][0]==edges[1][1]){
          return edges[0][0];
      }
      return edges[0][1];
    }
}
// @lc code=end

