import java.util.ArrayList;
import java.util.Stack;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode id=145 lang=java
 *
 * [145] Binary Tree Postorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
       Stack<TreeNode> stack = new Stack<TreeNode>(); 
       ArrayList<Integer> postOrder = new ArrayList<Integer>();
       if (root==null){
          return postOrder;
       }
      stack.push(root);

      while (!stack.empty()) {
          
        TreeNode curr = stack.pop();

        postOrder.add(0, curr.val);
        if(curr.left!=null){
            stack.push(curr.left);
        }
        if(curr.right!=null){
            stack.push(curr.right)  ;
        }
      }

      return postOrder;

    }
}
// @lc code=end

