import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

import org.w3c.dom.Node;

/*
 * @lc app=leetcode id=589 lang=java
 *
 * [589] N-ary Tree Preorder Traversal
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> preorder(Node root) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        Stack<Node> ans = new Stack<Node>();


        if (root == null) {
            return arr;
        }

        ans.push(root);

        while (!ans.isEmpty()) {

            Node curr = ans.pop();
            arr.add(curr.val);
            List<Node> nextNodes = curr.children;
            if (!nextNodes.isEmpty()) {

                Collections.reverse(nextNodes);
                for (Node node : nextNodes) {
                    ans.push(node);
                }
            }

        }

        return arr;

    }
}
// @lc code=end
