import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode id=235 lang=java
 *
 * [235] Lowest Common Ancestor of a Binary Search Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        TreeNode temp = root;

        while (temp != null) {
            if ((temp.val >= p.val && temp.val <= q.val) || (temp.val >= q.val && temp.val <= p.val)) {
                return temp;
            } else if (temp.val >= p.val) {
                temp = temp.left;
            } else {
                temp = temp.right;
            }
        }
        return null;

    }
}
// @lc code=end
