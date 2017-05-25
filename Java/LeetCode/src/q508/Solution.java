package q508;

import java.util.HashMap;
import java.util.ArrayList;

public class Solution {
	HashMap<Integer, Integer> result = new HashMap<Integer, Integer>();
    public int[] findFrequentTreeSum(TreeNode root) {
    	int[] finalResult;
        if(root == null){
        	finalResult = new int[0];
        	return finalResult;
        }
        helper(root);
        ArrayList<Integer> tempResult = new ArrayList<>();
        int maxValue = Integer.MIN_VALUE;
        for(int key:result.keySet()){
        	if(result.get(key) > maxValue){
        		maxValue = result.get(key);
        		tempResult.clear();
        		tempResult.add(key);
        	}else if (result.get(key) == maxValue){
        		tempResult.add(key);			
			}
        }
        finalResult = new int[tempResult.size()];
        int index = 0;
        for(int item:tempResult){
        	finalResult[index] = item;
        	index += 1;
        }
        return finalResult;
    }
    public int helper(TreeNode node){
    	int left = 0;
    	int right = 0;
    	int temp;
    	if(node.left != null){
    		left = helper(node.left);
    	}
    	if(node.right != null){
    		right = helper(node.right);
    	}
    	temp = left + right + node.val;
    	if(result.containsKey(temp)){
    		result.put(temp, result.get(temp)+1);
    	}else{
    		result.put(temp, 1);
    	}
    	return temp;
    }
}