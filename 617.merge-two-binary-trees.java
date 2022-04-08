import java.util.ArrayList;
import java.util.Queue;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode id=617 lang=java
 *
 * [617] Merge Two Binary Trees
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



    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        

ArrayList<Integer> bfs1 = breathFirstSearch(root1);
ArrayList<Integer> bfs2 = breathFirstSearch(root2);
int l1 = bfs1.size()    ;
int l2 = bfs2.size()    ;
int min = Math.min(l1, l2);
int i=0;
TreeNode root = new TreeNode(0); 
while (i<min) {
    TreeNode node = new TreeNode(bfs1.get(i)+bfs2.get(i));

}

    }
}
// @lc code=end

