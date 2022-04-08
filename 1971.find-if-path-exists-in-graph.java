import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/*
 * @lc app=leetcode id=1971 lang=java
 *
 * [1971] Find if Path Exists in Graph
 */

// @lc code=start
class Solution {

    // DEPTH FIRST SEARCH
    public boolean dfs(ArrayList<ArrayList<Integer>> adj, int source, int designation) {
        Stack<Integer> dfsStack = new Stack<Integer>();
        dfsStack.add(source);
boolean[] visited = new boolean[adj.size()];
        while (!dfsStack.isEmpty()) {
            int hold = dfsStack.pop();

            for (Integer elemiInteger : adj.get(hold)) {
                if(visited[elemiInteger]){
                    continue;
                }
                visited[elemiInteger]=true;

                if (elemiInteger == designation) {
                    return true;
                }
                
                dfsStack.push(elemiInteger);
            }
        }
        return false;
    }

    public ArrayList<ArrayList<Integer>> makeAdjacencyList(int[][] edges, int n) {
        ArrayList<ArrayList<Integer>> am = new ArrayList<ArrayList<Integer>>(n);

        for (int i = 0; i < n; i++)
            am.add(new ArrayList<Integer>());

        for (int[] edge : edges) {
            am.get(edge[0]).add(edge[1]);
            am.get(edge[1]).add(edge[0]);
        }

        return am;

    }

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        ArrayList<ArrayList<Integer>> adj = makeAdjacencyList(edges, n);
        if (source == destination) {
            return true;
        }
        return dfs(adj, source, destination);

    }
}
// @lc code=end
