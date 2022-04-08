import java.util.ArrayList;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode id=98 lang=java
 *
 * [98] Validate Binary Search Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {

    TreeNode previsousNode;

    public boolean inOrder(TreeNode root) {
        if (root == null) {
            return true;
        }
        if (!inOrder(root.left)) {
            return false;

        }

        if (previsousNode != null && previsousNode.val >= root.val) {
            return false;
        }
       previsousNode= root;
       return inOrder(root.right);

    }

    public boolean isValidBST(TreeNode root) {
previsousNode=null  ;
return inOrder(root);

    }
}
// @lc code=end
