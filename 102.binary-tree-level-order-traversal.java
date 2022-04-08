import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import javax.swing.tree.TreeNode;

import apple.laf.JRSUIUtils.Tree;

/*
 * @lc app=leetcode id=102 lang=java
 *
 * [102] Binary Tree Level Order Traversal
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

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
if(root==null){
    return  ans;
}
        Queue<TreeNode> bfs = new LinkedList<TreeNode>();
        bfs.add(root);
        while (!bfs.isEmpty()) {
            List<Integer> temp = new ArrayList<Integer>();
            Queue<TreeNode> temp2 = new LinkedList<TreeNode>();
            while (!bfs.isEmpty()) {
                TreeNode hold = bfs.remove();
                temp.add(hold.val);
                if (hold.left != null) {

                    temp2.add(hold.left);
                }
                if (hold.right != null) {

                    temp2.add(hold.right);
                }
            }
            ans.add(temp);
            bfs.addAll(temp2);

        }
        return ans;

    }
}
// @lc code=end
