package q105;

import java.util.Arrays;

//Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
    	int length = preorder.length;
    	if(length==0){
    		return null;
    	}else if (length==1) {
			return new TreeNode(preorder[0]);
		}
    	int value = preorder[0];
    	int index = 0;
    	for(int i=0;i<length;i++){
    		if(inorder[i]==value){
    			index = i;
    			break;
    		}
    	}
    	TreeNode node = new TreeNode(value);
    	node.left = buildTree(Arrays.copyOfRange(preorder, 1, index+1), Arrays.copyOfRange(inorder, 0, index));
    	node.right = buildTree(Arrays.copyOfRange(preorder, index+1, length), Arrays.copyOfRange(inorder, index+1, length));
        return node;
    }
    public static void main(String[] args) {
    	int[] preorder = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    	int[] inorder = {4, 3, 5, 2, 6, 1, 8, 7, 9};
    	Solution solution = new Solution();
    	TreeNode node = solution.buildTree(preorder, inorder);
    }
}