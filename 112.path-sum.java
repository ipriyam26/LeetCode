/*
 * @lc app=leetcode id=112 lang=java
 *
 * [112] Path Sum
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
    public boolean hasPathSum(TreeNode root, int targetSum) {

if(root==null){
   
        return false;
}

        return lengthOfTree(root, targetSum, 0);
    }


    public boolean lengthOfTree(TreeNode root, int targetSum,int currentSum) {
        if (root.left == null && root.right == null) {
            return targetSum==currentSum+root.val;
        }
        boolean minLeft=false,minRight=false;
        if (root.left != null) {

         minLeft = lengthOfTree(root.left, targetSum,currentSum+root.val);
        }
        if (root.right != null) {

         minRight = lengthOfTree(root.right, targetSum,currentSum+root.val);
        }
        return minLeft || minRight;
    }
}
// @lc code=end

