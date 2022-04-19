import java.util.ArrayList;
import java.util.Arrays;
import java.util.function.IntFunction;

/*
 * @lc app=leetcode id=210 lang=java
 *
 * [210] Course Schedule II
 */

// @lc code=start
class Solution {

    boolean[] inStack;
    boolean[] visited;
    ArrayList<Integer> order = new ArrayList<Integer>();

    public HashMap<Integer, ArrayList<Integer>> makeAdjacencyList(int[][] pre, int numCourses) {

        HashMap<Integer, ArrayList<Integer>> adj = new HashMap<Integer, ArrayList<Integer>>();

        for (int i = 0; i < numCourses; i++) {
            adj.put(i, new ArrayList<Integer>());
        }

        for (int[] course : pre) {
            adj.get(course[0]).add(course[1]);
        }

        return adj;
    }

    public boolean detectCycle(int start, HashMap<Integer, ArrayList<Integer>> adj) {
        if (inStack[start]) {
            // already inStack
            return false;
        }
        if (visited[start]) {
            return true;
        }
        inStack[start] = true;
        visited[start] = true;

        for (Integer elemInteger : adj.get(start)) {
            if (!detectCycle(elemInteger, adj)) {
                return false;
            }
        }
        order.add(start);
        inStack[start] = false;

        return true;

    }

    public boolean iterateMap(HashMap<Integer, ArrayList<Integer>> adj) {
        for (HashMap.Entry<Integer, ArrayList<Integer>> b : adj.entrySet()) {
            int curr = b.getKey();
            if (visited[curr]) {
                continue;
            }
            if (!detectCycle(curr, adj)) {
                return false;
            }

        }
        return true;
    }

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        inStack = new boolean[numCourses];
        visited = new boolean[numCourses];
        int[] arr = new int[numCourses];
        if (numCourses == 0) {
            return arr;
        }

        if (!iterateMap(makeAdjacencyList(prerequisites, numCourses))) {
            return new int[0];
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] = order.get(i);
        }
        return arr;
    }
}
// @lc code=end
