/**
 * @author zhangchi
 *
 * 2017年9月28日 上午1:27:06
 */
package amazon;

import java.util.HashMap;

/**
 * @author zhangchi
 * 2017年9月28日 上午1:27:06
 */
public class TwoSum {
	public int[] twoSum(int[] nums, int target) {
        int length = nums.length;
        int[] result = new int[2];
        //HashSet<Integer> check = new HashSet<Integer>();
        HashMap<Integer, Integer> check = new HashMap<Integer, Integer>();
        for(int i=0;i<length;i++){
            if(check.containsKey(target-nums[i])){
                result[0] = check.get(target-nums[i]);
                result[1] = i;
                return result;
            }else{
                check.put(nums[i],i);
            }
        }
        return null;
    }
}
