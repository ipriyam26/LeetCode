import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;

class Solution {

    boolean[] inStack;
    boolean[] visited;

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

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses == 1 || numCourses == 0)
            return true;
        if (prerequisites.length == 0)
            return true;

        inStack = new boolean[numCourses];
        visited = new boolean[numCourses];
        return iterateMap(makeAdjacencyList(prerequisites, numCourses));
    }

}