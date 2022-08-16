import java.util.ArrayList;
import java.util.Stack;
import javafx.util.Pair;  

/*
 * @lc app=leetcode id=1129 lang=java
 *
 * [1129] Shortest Path with Alternating Colors
 */

// @lc code=start
class Solution {

    class Path{
        int color;
        int directedNode;
        Path(int color, int directedNode){
            this.color = color;
            this.directedNode = directedNode;
        }
    }
    
    public ArrayList<ArrayList<Path>> makeAdjacencyList(int[][] red, int[][] blue, int num) {
        ArrayList<ArrayList<Path>> adj = new ArrayList<ArrayList<Path>>();

        for (int i = 0; i < num; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] course : red) {
            adj.get(course[0]).add(new Path(0, course[1]));
            // adj.get(course[1]).add(course[0]);

        }
        for (int[] course : blue) {
            adj.get(course[0]).add(new Path(1, course[1]));
            // adj.get(course[1]).add(course[0]);

        }

        return adj;
    }

    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        ArrayList<ArrayList<Path>> graph = makeAdjacencyList(redEdges, blueEdges, n);
        int[] ans = new int[n];
        ans[0]= 0;
        Stack<Pair<Path,Integer>> bfs = new Stack<Pair<Path,Integer>>();

        bfs.push

    }
}
// @lc code=end

