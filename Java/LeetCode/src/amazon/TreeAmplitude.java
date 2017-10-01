/**
 * @author zhangchi
 *
 * 2017年9月30日 下午1:10:39
 */
package amazon;

/**
 * @author zhangchi
 * 2017年9月30日 下午1:10:39
 */
public class TreeAmplitude {
	int result = Integer.MIN_VALUE;
	public int solution(TreeNode root) {
		if(root==null){return 0;}
		helper(root, root.val, root.val);
		int re = result;
		result = Integer.MIN_VALUE;
		return re;
	}
	
	public void helper(TreeNode node, int min, int max){
		// 从上到下，不断更新最大最小值
		if(node.val<min){min=node.val;}
		if(node.val>max){max=node.val;}
		result = Math.max(result, max-min);
		if(node.left!=null){helper(node.left, min, max);}
		if(node.right!=null){helper(node.right, min, max);}
	}
	
	public static void main(String[] args){
		TreeAmplitude treeAmplitude = new TreeAmplitude();
		// data come from: http://siyang2notleetcode.blogspot.ca/2015/02/amplitude-of-tree.html
		TreeNode node = new TreeNode(5);
		node.left = new TreeNode(8);
		node.right = new TreeNode(10);
		node.left.left = new TreeNode(12);
		node.left.right = new TreeNode(2);
		node.right.left = new TreeNode(8);
		node.right.right = new TreeNode(4);
		node.right.left.left = new TreeNode(2);
		node.right.right.left = new TreeNode(5);
		System.out.println(treeAmplitude.solution(node));
	}
}
