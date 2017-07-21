package q107;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

//Definition for a binary tree node.
class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode(int x) { val = x; }
}

public class Solution {
	public static void main(String[] args){
		TreeNode node = new TreeNode(3);
		node.left = new TreeNode(9);
		node.right = new TreeNode(20);
		node.right.left = new TreeNode(15);
		node.right.right = new TreeNode(7);
		Solution s = new Solution();
		s.levelOrderBottom(node);
	}
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
    	if(root==null){
    		return new ArrayList<>();
    	}
    	Stack<List<Integer>> result = new Stack<>();
    	List<TreeNode> now = new ArrayList<>();
    	List<TreeNode> next = new ArrayList<>();
    	now.add(root);
    	List<Integer> value = new ArrayList<>();
    	while(now.isEmpty()==false){
	    	for(TreeNode node:now){
	    		value.add(node.val);
	    		if(node.left!=null){
	    			next.add(node.left);
	    		}
	    		if(node.right!=null){
	    			next.add(node.right);
	    		}
	    	}
	    	result.push(value);
	    	value = new ArrayList<Integer>();
	    	now = next;
	    	next = new ArrayList<>();
    	}
    	List<List<Integer>> finalResult = new ArrayList<>();
    	while(result.isEmpty()==false){
    		finalResult.add(result.pop());
    	}
        return finalResult;
    }
}
