/**
 * @author zhangchi
 *
 * 2017年9月28日 下午12:07:57
 */
package amazon;

class TreeNode {
	     int val;
	     TreeNode left;
	     TreeNode right;
	     TreeNode(int x) { val = x; }
	 }

/**
 * @author zhangchi
 * 2017年9月28日 下午12:07:57
 */
public class SubtreeofAnotherTree {
	public boolean isSubtree(TreeNode s, TreeNode t) {
        if(s == null){
            return false;
        }else if(s.val == t.val && helper(s.left,t.left) && helper(s.right,t.right)){
            return true;
        }else{
            return isSubtree(s.left, t) || isSubtree(s.right, t);
        }
    }
    public boolean helper(TreeNode s, TreeNode t){
        if(s == null && t == null){
            return true;
        }else if(s == null || t == null){
            return false;
        }else if(s.val == t.val){
            return (helper(s.left,t.left) && helper(s.right,t.right));
        }else{
            return false;
        }
    }
}
