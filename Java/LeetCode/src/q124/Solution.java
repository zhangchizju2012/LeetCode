/**
 * @author zhangchi
 *
 * 2017年8月2日 下午12:16:21
 */
package q124;


//Definition for a binary tree node.
class TreeNode {
int val;
TreeNode left;
TreeNode right;
TreeNode(int x) { val = x; }
}
// 重新写发现跟当初写的一模一样
public class Solution {
	int result = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
    	if(root==null){
    		return 0;
    	}
        helper(root);
        return result;
    }
    public int helper(TreeNode node) {
    	int left = Integer.MIN_VALUE;
    	int right = Integer.MIN_VALUE;
    	if(node.left!=null){
    		left = helper(node.left);
    	}
    	if(node.right!=null){
    		right = helper(node.right);
    	}
    	result = Math.max(result, Math.max(0, left)+Math.max(0, right)+node.val);
    	return Math.max(Math.max(left, right),0)+node.val;
    }
}
