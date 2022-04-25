import java.util.ArrayList;
import java.util.Arrays;

/*
 * @lc app=leetcode id=886 lang=java
 *
 * [886] Possible Bipartition
 */

// @lc code=start
class Solution {
    int visited[];

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

    public boolean dfs(ArrayList<ArrayList<Integer>> graph, int current, int color) {
        visited[current] = color;
        for (int neighbor : graph.get(current)) {
            if (visited[neighbor] == 0) {
                if (!dfs(graph, neighbor, 3 - color)) {
                    return false;
                }
            }
            if (visited[neighbor] == visited[current]) {
                // System.out.println(neighbor+" "+current);
                return false;
            }
        }
        return true;
    }

    public boolean possibleBipartition(int n, int[][] dislikes) {
        ArrayList<ArrayList<Integer>> graph = makeAdjacencyList(dislikes, n + 1);
        visited = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            
            // System.out.println(i);
            if (visited[i] == 0) {
                if (!dfs(graph, i, 1)) {
                    return false;
                }
            }

        }
        return true;
    }
}

// @lc code=end
