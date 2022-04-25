import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/*
 * @lc app=leetcode id=802 lang=java
 *
 * [802] Find Eventual Safe States
 */

// @lc code=start
class Solution {

    // int[] check;

    // public boolean check_node(int current, int[][] graph, HashMap<Integer, Boolean> terminal, boolean[] visited) {
    //     if(check[current] != 0) return check[current] == 1;

    //     if (terminal.containsKey(current)) {
    //         return true;
    //     }
    //     if (visited[current]) {
    //         return false;
    //     } else {
    //         visited[current] = true;
    //     }
        
    //     for (Integer neighbor : graph[current]) {

    //         if (!check_node(neighbor, graph, terminal, visited)) {
    //             check[current] = -1;
    //             return false;
    //         }
    //     }
    //     check[current] = 1;
    //     return true;

    // }

    // public List<Integer> eventualSafeNodes(int[][] graph) {

    //     int n = graph.length;
    //     HashMap<Integer,Boolean> terminal = new HashMap<>();
    //     List<Integer> ans = new ArrayList<>();
    //     check = new int[n];

    //     for (int i = 0; i < n; i++) {
    //         if (graph[i].length == 0) {
    //             terminal.put(i, true);
    //         }
    //     }
    //     boolean[] visited = new boolean[n];
    //     for (int i = 0; i < n; i++) {
    //         if (check_node(i, graph, terminal, visited)) {
    //             ans.add(i);
    //         }
            
    //     }
    //     return ans;

    // }
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length, color[] = new int[n];
        List<Integer> res = new ArrayList<>();
        
        for(int i = 0; i < n; i++) {
            if(dfs(graph, color, i)) res.add(i);
        }
        
        return res;
    }
    
    private boolean dfs(int[][] graph, int[] color, int node) {
        if(color[node] != 0) return color[node] == 2;
        
        color[node] = 1;
        
        for(int neighbor : graph[node]) {
            if(!dfs(graph, color, neighbor)) return false;
        }
        
        color[node] = 2;
        
        return true;
    }

}
// @lc code=end
