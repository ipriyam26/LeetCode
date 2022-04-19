import java.util.ArrayList;

/*
 * @lc app=leetcode id=684 lang=java
 *
 * [684] Redundant Connection
 */

// @lc code=start
class Solution {
    int[] inStack;
    boolean[] visited;
    int ans = 0;

    public ArrayList<ArrayList<Integer>> makeAdjacencyList(int[][] pre, int num) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i <= num; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] course : pre) {
            adj.get(course[0]).add(course[1]);
            adj.get(course[1]).add(course[0]);

        }

        return adj;
    }

    public boolean detectCycle(int start, ArrayList< ArrayList<Integer>> adj) {
        if (inStack[start]>2) {
            // already inStack
            ans = start;
            return false;
        }
        if (visited[start]) {
            return true;
        }
        inStack[start] ++;
        visited[start] = true;

        for (Integer elemInteger : adj.get(start)) {
            if (!detectCycle(elemInteger, adj)) {
                return false;
            }
        }
        inStack[start]--;

        return true;

    }

    public int[] findRedundantConnection(int[][] edges) {
        ArrayList<ArrayList<Integer>> adj = makeAdjacencyList(edges, edges.length);
        inStack = new int[edges.length+1];
        
        visited = new boolean[edges.length+1];
        int[] ss = new int[2];
        for (int i = 1; i < adj.size(); i++) {
            if (visited[i]) {
                continue;
            }
            if (!detectCycle(i, adj)) {
                ss[0] = i;
                ss[1] = ans;
                System.out.println("ff");
                break;
            }
        }
        return ss;
    }
}

// @lc code=end
