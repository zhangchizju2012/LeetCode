/**
 * @author zhangchi
 *
 * 2017年10月1日 下午1:26:46
 */
package amazon;

import java.util.*;

/**
 * @author zhangchi
 * 2017年10月1日 下午1:26:46
 */
// 利用PriorityQueue
public class SlidingWindowMaximum {
	public int[] maxSlidingWindow(int[] nums, int k) {
        int length = nums.length;
        if(length==0){return nums;}
        int[] result = new int[length - k + 1];
        int now;
        int previous;
        PriorityQueue<Integer> temp = new PriorityQueue<Integer>(Collections.reverseOrder());
        HashMap<Integer, Integer> removed = new HashMap<Integer, Integer>();
        // 存放已经移除的
        for(int i = 0; i < k - 1; i ++){//少加了一个，配合line 29
            temp.offer(nums[i]);
        }
        for(int i = 0; i < length - k + 1; i++){
            temp.offer(nums[i+k-1]);
            now = temp.peek();
            while(removed.containsKey(now) && removed.get(now)>0){
            // 检查是否已经被移除了
                removed.put(now,removed.get(now)-1);
                temp.poll();
                now = temp.peek();
            }
            result[i] = now;
            previous = nums[i];
            if(removed.containsKey(previous)){
                removed.put(previous,removed.get(previous)+1);
            }else{
                removed.put(previous,1);
            }
        }
        return result;
    }
}
