package q113;

import java.util.ArrayList;
import java.util.List;

//Definition for a binary tree node.
class TreeNode {
int val;
TreeNode left;
TreeNode right;
TreeNode(int x) { val = x; }
}

public class Solution {
	List<List<Integer>> result = new ArrayList<>();
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if(root==null){
        	return new ArrayList<>();
        }
        helper(root, sum, new ArrayList<>());
        return result;
    }
    public void helper(TreeNode node, int sum, List<Integer> before){
    	List<Integer> now = new ArrayList<>(before);
    	now.add(node.val);
    	if(sum==node.val && node.left==null && node.right==null){
    		result.add(now);
    	}else{
    		if(node.left!=null){
    			helper(node.left, sum-node.val, now);
    		}
    		if(node.right!=null){
    			helper(node.right, sum-node.val, now);
    		}
    	}
    }
}
