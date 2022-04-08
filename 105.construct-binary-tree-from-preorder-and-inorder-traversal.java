import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

/*
 * @lc app=leetcode id=105 lang=java
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
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

    Queue<Integer> pres = new LinkedList<Integer>();

    public int findIndexOf(int[] arr, int search) {
        int i = 0;
        while (search != arr[i]) {
            i++;
        }
        return i;
    }
    public TreeNode makeTree(int[] inorder) {
        if (inorder.length == 1) {
            return new TreeNode(pres.remove());
        }


        TreeNode root = new TreeNode(pres.remove());
        int index = findIndexOf(inorder, root.val);
       int[] left= Arrays.copyOfRange(inorder, 0, index);
       if(left.length>0){

           root.left = makeTree(left);
       }
        int[] right = Arrays.copyOfRange(inorder, index + 1, inorder.length);
        if(right.length>0){

            root.right = makeTree(right);
        }
        return root;

    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
for (int integer : preorder) {
    pres.add(integer);
}
  
        return makeTree(inorder);
    }
}
// @lc code=end
