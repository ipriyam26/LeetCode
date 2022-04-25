import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;

/*
 * @lc app=leetcode id=743 lang=java
 *
 * [743] Network Delay Time
 */

// @lc code=start
class Solution {

    class Cell implements Comparable<Cell> {
        int node, time;
        Cell(int node, int time) {
            this.node = node;
            this.time = time;
        }    
        public int compareTo(Cell c2) {
            return  time-c2.time;
        }
    }



    public int networkDelayTime(int[][] times, int n, int k) {
     HashMap<Integer,List<Cell>> graph = new HashMap();
     boolean[] visited = new boolean[n+1];
     for (int[] edge : times) {
         graph.computeIfAbsent(edge[0], v->new ArrayList<>()).add( new Cell(edge[1],edge[2]));
     }
     Map<Integer, Integer> costs = new HashMap<>();
     PriorityQueue<Cell> heap = new PriorityQueue<Cell>();
     heap.add(new Cell(k, 0));
        
     while(!heap.isEmpty()) {
         Cell curr = heap.poll();
         if(costs.containsKey(curr.node)) continue;
         costs.put(curr.node, curr.time);
         
         if (graph.containsKey(curr.node))  {
             for(Cell neig: graph.get(curr.node)) {
                 if (!costs.containsKey(neig.node)) {
                     heap.add(new Cell(neig.node, neig.time+curr.time));
                 }
             }
         }
     }
     int ans = -1;
     if (costs.size() != n) return ans;
     for (int cost: costs.values()) {
         ans  = Math.max(ans, cost);
     }
     return ans;     
        
    }
}
// @lc code=end

