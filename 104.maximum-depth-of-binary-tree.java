/*
 * @lc app=leetcode id=104 lang=java
 *
 * [104] Maximum Depth of Binary Tree
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

    public int maxDepth(TreeNode root) {
        if(root==null){
            return 0;
        }
return lengthOfTree(root, 1, 1);
    }

    public int lengthOfTree(TreeNode root, int max, int currentLength) {
        if (root == null) {
            return max;
        }
        
        int maxLeft = lengthOfTree(root.left, Math.max(max,currentLength), currentLength+1);
        int maxRight = lengthOfTree(root.right, Math.max(max, currentLength), currentLength+1);
        return Math.max(maxLeft, maxRight);
    }
}
// @lc code=end
