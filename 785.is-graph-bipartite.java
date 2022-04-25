import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

/*
 * @lc app=leetcode id=785 lang=java
 *
 * [785] Is Graph Bipartite?
 */

// @lc code=start
class Solution {
    public boolean isBipartite(int[][] graph) {

        Set<Integer> set1 = new HashSet<Integer>();
        Set<Integer> set2 = new HashSet<Integer>();
        Queue<Integer> bfs = new LinkedList<Integer>();
        boolean[] visited = new boolean[graph.length];
        // visited[0]=true;
        for (int i = 0; i < graph.length; i++) {
            if(visited[i]){
                continue;
            }
            bfs.add(i);

            while (!bfs.isEmpty()) {
                int pop = bfs.poll();
                if(visited[pop]){
                    continue;
                }
                visited[pop]=true;
                
                if(graph[pop].length==0){
                    continue;
                }
                if (set1.contains(pop)) {
    
                    for (Integer integer : graph[pop]) {
                        if (set1.contains(integer)) {
                            return false;
                        } else {
                            set2.add(integer);
                        }
                    }
    
                } else if (set2.contains(pop)) {
                    for (Integer integer : graph[pop]) {
                        if (set2.contains(integer)) {
                            return false;
                        } else {
                            set1.add(integer);
                        }
                    }
                } else {
                    set1.add(pop);
                    for (Integer integer : graph[pop]) {
                        set2.add(integer);
                    }
                }
    
                for (Integer b : graph[pop]) {
    
                  bfs.add(b);
                }
                
    
            }
        }

        // if (set1.size() + set2.size() != graph.length) {
        //     return false;
        // }
        return true;
    }
}
// @lc code=end
