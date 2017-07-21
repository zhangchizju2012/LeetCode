package q112;

import java.util.ArrayList;

//Definition for a binary tree node.
class TreeNode {
int val;
TreeNode left;
TreeNode right;
TreeNode(int x) { val = x; }
}

public class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
    	if(root==null){
            return false;
        }
    	ArrayList<TreeNode> now = new ArrayList<>();
    	ArrayList<TreeNode> next = new ArrayList<>();
    	TreeNode node;
    	node = root;
    	node.val = sum - node.val;
    	now.add(node);
    	while(now.isEmpty()==false){
    		for(TreeNode n:now){
    			if(n.val==0 && n.left==null && n.right==null){
    				return true;
    			}
    			if(n.left!=null){
    				node = n.left;
    				node.val = n.val - node.val;
    				next.add(node);
    			}
    			if(n.right!=null){
    				node = n.right;
    				node.val = n.val - node.val;
    				next.add(node);
    			}
    		}
    		now = next;
    		next = new ArrayList<>();
    	}
        return false;
    }
}