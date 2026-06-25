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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (subRoot == null) return true;
        if (root == null) return false;
        
        boolean sameroot = root.val == subRoot.val;
        return (sameroot && isSametree(root, subRoot)) 
        || isSubtree(root.left, subRoot)
        || isSubtree(root.right, subRoot);
    }

    private boolean isSametree(TreeNode root, TreeNode subRoot) {
        if (subRoot == null || root == null) return root == null && subRoot == null;
        return root.val == subRoot.val && isSametree(root.left, subRoot.left)
        && isSametree(root.right, subRoot.right);
    }
}
