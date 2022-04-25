import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;

/*
 * @lc app=leetcode id=684 lang=java
 *
 * [684] Redundant Connection
 */

// @lc code=start
class Solution {
int[] cycle;

    int CycleStart = -1;

public HashMap<Integer,ArrayList<Integer>> makeAdjacencyList(int[][] pre, int numCourses)   {
    HashMap<Integer,ArrayList<Integer>> adj = new HashMap<Integer,ArrayList<Integer>>();

    for (int i = 0; i < numCourses; i++) {
        adj.put(i, new ArrayList<Integer>());
    }

    for (int[] course : pre) {
        adj.get(course[0]).add(course[1]);
    }

    return adj;
}

    void dfs(HashMap<Integer,ArrayList<Integer>> ADJ, boolean[] visited, int curr, int parent) {
        if (visited[curr]) {
            CycleStart = curr;
            return;
        }
        visited[curr] = true;
        for (Integer elemInteger : ADJ.get(curr)) {
            if (curr == parent) {
                continue;
            }
            if (CycleStart==-1) {
                dfs(ADJ, visited, elemInteger, curr);
            }
            if (CycleStart != -1) {
                cycle[curr]++;
            }
            if (curr == CycleStart) {
                CycleStart = -1;
                return;
            }
        }

    }

    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        HashMap<Integer,ArrayList<Integer>> ADJ = makeAdjacencyList(edges, n+1);
        cycle = new int[n+1];
        dfs(ADJ, new boolean[n+1], 1, -1);

        
       for (int i = n-1; i >0; i--) {
          if(cycle[edges[i][0]]>1 && cycle[edges[i][1]]>1){
              return edges[i];
          }
       }
       return  new int[2];

       

    }
}

// @lc code=end
