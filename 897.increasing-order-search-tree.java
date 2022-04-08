/*
 * @lc app=leetcode id=897 lang=java
 *
 * [897] Increasing Order Search Tree
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
    public TreeNode increasingBST(TreeNode root) {

        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode head = new TreeNode(); 

        TreeNode ans = head;
        TreeNode curr = root;
        while (!stack.empty() || curr != null) {

            if (curr != null) {
                stack.push(curr);
                curr = curr.left;
            } else {
                curr = stack.pop();
                ans.right = curr;
                ans = ans.right;
                curr = curr.right;

            }
        }
        while(head!=null){
            System.out.println(head.val);
            head=head.right;
        }
        return head;

    }
}
// @lc code=end
