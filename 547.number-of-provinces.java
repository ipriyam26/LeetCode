import java.util.ArrayList;
import java.util.Arrays;

/*
 * @lc app=leetcode id=547 lang=java
 *
 * [547] Number of Provinces
 */

// @lc code=start
class Solution {

    boolean[] visited;



    public void DFS(int row, int[][] graph) {

        for (int col = 0; col < graph.length; col++) {
            if (graph[row][col] == 1 && !visited[col]) {

                visited[col] = true;
                DFS(col, graph);
            }
        }

    }

    public int findCircleNum(int[][] isConnected) {

        int n = isConnected.length;
        if (n == 0 ||   isConnected[0].length == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        visited = new boolean[n];
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                DFS(i, isConnected);
                count++;
            }
        }
        return count;

    }
}
// @lc code=end
