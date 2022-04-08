import java.util.ArrayList;

/*
 * @lc app=leetcode id=101 lang=java
 *
 * [101] Symmetric Tree
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
/* Proposed solution as of now:
1. Find the In-order of the tree.
2. Go to the middle point.(Ignore it)
3. Now make two pointers and move forward with one and backwards with the other 
4. If they don't match they aren't similar.
5. If they both reach end with out getting to an they are symmetric

*/

/* Optimal solution as of now:
1. Split the root into two tree for left and right.
2. compare each value keep in mind left==right
*/

class Solution{
    public boolean isSymmetric(TreeNode root) {
        if(root==null)return true;
        return isMirrorImage(root.left,root.right);
    }
    private boolean isMirrorImage(TreeNode r1,TreeNode r2){
        if(r1==null && r2==null)return true;
        else if(r1==null || r2==null)return false;
        return r1.val==r2.val && isMirrorImage(r1.left,r2.right) && isMirrorImage(r1.right,r2.left);
    }
} 
// @lc code=end

