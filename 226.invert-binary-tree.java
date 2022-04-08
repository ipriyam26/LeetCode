import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode id=226 lang=java
 *
 * [226] Invert Binary Tree
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

public void invert(TreeNode root){

    if(root==null){
        return;
    }
    if(root.left==null && root.right==null){
        return;
    }
    TreeNode childL = root.left;
    TreeNode childR = root.right;
    root.left = childR;
    root.right =childL;
     invertTree(root.left);
     invertTree(root.right);
}

    public TreeNode invertTree(TreeNode root) {
    invert(root);
    return root;

    }
}
// @lc code=end

