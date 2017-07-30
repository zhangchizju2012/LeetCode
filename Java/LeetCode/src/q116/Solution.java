/**
 * @author zhangchi
 *
 * 2017年7月30日 下午5:20:58
 */
package q116;

/**
 * @author zhangchi
 * 2017年7月30日 下午5:20:58
 */

// Definition for binary tree with next pointer.
class TreeLinkNode{
	int val;
	TreeLinkNode left, right, next;
	TreeLinkNode(int x) { val = x; }
}

public class Solution {
    public void connect(TreeLinkNode root) {
    	if(root!=null){
    		helper(root);
    	}
    }
    public void helper(TreeLinkNode root) {
    	TreeLinkNode nextLeft = root.left;
    	TreeLinkNode nextRight = root.right;
    	if(nextLeft!=null){
    		helper(nextLeft);
    		helper(nextRight);
    		// 将左右两子树相靠近的节点连接在一起
    		while(nextLeft!=null){
    			nextLeft.next = nextRight;
    			nextLeft = nextLeft.right;
    			nextRight = nextRight.left;
    		}
    	}
    	
    }
}