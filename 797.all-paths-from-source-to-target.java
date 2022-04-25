import java.util.ArrayList;
import java.util.Stack;

/*
 * @lc app=leetcode id=797 lang=java
 *
 * [797] All Paths From Source to Target
 */

// @lc code=start

class Solution {

//     Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

// The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
    
    class node{
        int id;
        ArrayList<Integer> parents;
        node(int id, ArrayList<Integer> parents){
            this.id = id;
            this.parents = parents;
        }
    }

   
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>>  ans = new ArrayList<>();
        ArrayList<Integer> path = new ArrayList<>();
        path.add(0);
        Stack<node> stack = new Stack<>();
        stack.push(new node(0, path));
        while(!stack.isEmpty()) {
            node curr = stack.pop();

            if(curr.id == graph.length - 1) {
                ans.add(new ArrayList<>(curr.parents));
            }

            for(int i = 0; i < graph[curr.id].length; i++) {
                ArrayList<Integer> newPath = new ArrayList<>(curr.parents);
                newPath.add(graph[curr.id][i]);
                stack.push(new node(graph[curr.id][i], newPath));
            }
        }
        return ans;
        }
    }

// @lc code=end

