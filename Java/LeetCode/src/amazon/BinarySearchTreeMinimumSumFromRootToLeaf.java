/**
 * @author zhangchi
 *
 * 2017年9月28日 下午9:59:19
 */
package amazon;

/**
 * @author zhangchi
 * 2017年9月28日 下午9:59:19
 */
public class BinarySearchTreeMinimumSumFromRootToLeaf {
	public int Solution(TreeNode root) {
		if(root==null){return 0;}
		else{
			if(root.left==null && root.right==null){return root.val;}
			else{
				int left = Integer.MAX_VALUE;
				int right = Integer.MAX_VALUE;
				if(root.left!=null){
					left = root.val + Solution(root.left);
				}
				if(root.right!=null){
					right = root.val + Solution(root.right);
				}
				return Math.min(left,right);
			}
		}
	}
}
