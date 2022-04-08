import java.util.LinkedList;
import java.util.Queue;

import javax.swing.tree.TreeNode;

import apple.laf.JRSUIUtils.Tree;

/*
 * @lc app=leetcode id=114 lang=java
 *
 * [114] Flatten Binary Tree to Linked List
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

    Queue<TreeNode> preOrder = new LinkedList<TreeNode>();

    public void preOrder(TreeNode root) {

        if (root == null) {
            return;
        }
        preOrder.add(root);
        preOrder(root.left);
        preOrder(root.right);

    }

    public void flatten(TreeNode root) {

        preOrder(root);
        
TreeNode temp = root;
        while (!preOrder.isEmpty()) {
            TreeNode node = preOrder.remove();
            temp.right = node;
            temp = temp.right;
        }
        // root = root.right;

        while (root!=null) {
            System.out.println(root.val+" ");
            root=root.right;
        }

    }
}
// @lc code=end
