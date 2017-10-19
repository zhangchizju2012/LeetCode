/**
 * @author zhangchi
 *
 * 2017年7月28日 下午2:00:54
 */
package q16;

import java.util.ArrayList;
import java.util.Arrays;

//Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
//
//For example, given array S = {-1 2 1 -4}, and target = 1.
//
//The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
/**
 * @author zhangchi
 * 2017年7月28日 下午2:00:54
 */

// 还需要复习，只要完成n^2复杂度就可以了
public class Solution {
	public static void main(String[] args){
		Solution solution = new Solution();
		int[] nums = {-3,-2,-5,3,-4};
		int target = -1;
		System.out.println(solution.threeSumClosest(nums, target));
	}
    public int threeSumClosest(int[] nums, int target) {
    	Arrays.sort(nums);
    	ArrayList<Integer> newNums = new ArrayList<>();
    	int previous = nums[0];
    	int count = 1;
    	for(int i=1;i<nums.length;i++){
    		if(nums[i]==previous){
    			count += 1;
    		}else{
    			for(int j=0;j<Math.min(3, count);j++){
    				newNums.add(previous);
    			}
    			previous = nums[i];
    			count = 1;
    		}
    	}
    	for(int j=0;j<Math.min(3, count);j++){
			newNums.add(previous);
		}
    	int result = newNums.get(0)+newNums.get(1)+newNums.get(2);
    	int left;
		int middle;
		int right;
		int temp;
    	for(int i=0;i<newNums.size()-2;i++){
    		left = i;
    		middle = i+1;
    		right = newNums.size()-1;
    		while(middle<right){
    			temp = newNums.get(left) + newNums.get(middle) + newNums.get(right);
    			if(Math.abs(result-target)>Math.abs(temp-target)){
    				result = temp;
    			}
    			if(temp==target){
    				return temp;
    			}else if (temp<target) {
					middle += 1;
				}else {
					right -= 1;
				}
    		}
    	}
        return result;
    }
}
