/*
 * @lc app=leetcode id=543 lang=java
 *
 * [543] Diameter of Binary Tree
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

int max=0;
        public int lengthOfTree(TreeNode root) {
            if (root == null) {
                return 0;
            }
            int leftDepth = lengthOfTree(root.left);
            int rightDepth = lengthOfTree(root.right);
            max = Math.max(max,leftDepth+ rightDepth);
            return Math.max(leftDepth,rightDepth)+1;

            
            
        }


    public int diameterOfBinaryTree(TreeNode root) {
 lengthOfTree(root);
 return max;
    }
}
// @lc code=end

