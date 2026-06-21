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
    public int goodNodes(TreeNode root) {
        int count = 1;
        int max = root.val;

        return count + countGoodNodes(root.left, max) + countGoodNodes(root.right, max);
    }

        private int countGoodNodes(TreeNode root, int max) {
            if (root == null) {
                return 0;
            }
            System.out.println(root.val + max);
            if (root.val > max) {
                max = root.val;
            }

            int left = 0;
            if (root.left != null) {
                left = countGoodNodes(root.left, max);
            }
            int right = 0;
            if (root.right != null) {
                right = countGoodNodes(root.right, max);
            }
            if (root.val >= max) {
                return 1 + left + right;
            } 
            else {
                return left + right;
            }

        }
}
