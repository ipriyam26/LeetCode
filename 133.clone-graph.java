import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Stack;

import org.w3c.dom.Node;

/*
 * @lc app=leetcode id=133 lang=java
 *
 * [133] Clone Graph
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {

    public void dfs(Node current, Map<Integer, Node> hmac) {

        if (hmac.containsKey(current.val)) {
            return;
        }
        Node parent = new Node(current.val);
        hmac.put(parent.val, parent);
        for (Node neighbor : current.neighbors) {
            dfs(neighbor, hmac);
            Node child = hmac.get(neighbor.val);
            parent.neighbors.add(child);
        }

    }

    public Node cloneGraph(Node node) {
        Map<Integer, Node> hmac = new HashMap<Integer, Node>();

        if (node == null) {
            return null;
        }
        if (node.neighbors.size() == 0) {
            return new Node(1);
        }

        dfs(node, hmac);
        return hmac.get(1);
    }
}


// @lc code=end
