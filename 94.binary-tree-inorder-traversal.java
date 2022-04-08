/*
 * @lc app=leetcode id=94 lang=java
 *
 * [94] Binary Tree Inorder Traversal
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
import java.util.*;
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<Integer> stack = new Stack<Integer>();
        ArrayList inode = new ArrayList<Integer>();
        Node curr = root;
        while (!stack.empty()||curr!=null) {

            if(curr!=null){
                stack.push(curr);
                curr=curr.left; 
            }
            else{
                curr = stack.pop();

                inode.add(curr.val);

                curr=curr.right;

            }
        }
        return inode;


    }


}
// @lc code=end

