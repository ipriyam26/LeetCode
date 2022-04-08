/*
 * @lc app=leetcode id=111 lang=java
 *
 * [111] Minimum Depth of Binary Tree
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
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
;
        return lengthOfTree(root, 1);
    }

    public int lengthOfTree(TreeNode root, int currentLength) {
        if (root.left == null && root.right == null) {
            return currentLength;
        }
        int minLeft=Integer.MAX_VALUE,minRight=Integer.MAX_VALUE;
        if (root.left != null) {

         minLeft = lengthOfTree(root.left, currentLength + 1);
        }
        if (root.right != null) {

         minRight = lengthOfTree(root.right, currentLength + 1);
        }
        return Math.min(minLeft, minRight);
    }
}
// @lc code=end
