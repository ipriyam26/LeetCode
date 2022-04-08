import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Ans
 */

public class Ans {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    Queue<Integer> pres = new LinkedList<Integer>();
    private boolean addAll;

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

    public ArrayList<Integer> inOrderOfTree(TreeNode root) {
        if (root == null) {
            ArrayList<Integer> ans = new ArrayList<Integer>();
            return ans;
        }

        ArrayList<Integer> ans = new ArrayList<Integer>();
        addAll = ans.addAll(inOrderOfTree(root.left));
        ans.add(root.val);
        ans.addAll(inOrderOfTree(root.right));
        return ans;
    }

    public static void main(String[] args) {
        Ans obj = new Ans();
        int[] pre = { 1, 2 };
        int[] in = { 2, 1 };
        TreeNode root = obj.buildTree(pre, in);
        ArrayList<Integer> pp = obj.inOrderOfTree(root);
        System.out.println(pp.toString());
    }
}