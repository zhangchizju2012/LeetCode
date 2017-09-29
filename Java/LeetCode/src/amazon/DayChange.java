/**
 * @author zhangchi
 *
 * 2017年9月28日 下午9:42:16
 */
package amazon;

/**
 * @author zhangchi
 * 2017年9月28日 下午9:42:16
 */
import java.util.Arrays;

public class DayChange {
    public int[] Solution(int[] days, int n) {
        if (days == null || n <= 0) return days;
        int length = days.length;
        int[] rvalue = new int[length + 2];
        rvalue[0] = rvalue[length+1] = 0;
        for (int i = 1; i <= length; i++)
            rvalue[i] = days[i-1];
        for (int i = 0; i < n; i++) {
        	int pre = rvalue[0];//应该挪到24行之前吧
            for (int j = 1; j <= length; j++) {
                int temp = rvalue[j];
                rvalue[j] = pre ^ rvalue[j+1];
                pre = temp;
            }
        }
        return Arrays.copyOfRange(rvalue, 1, length+1);
    }
    
    public static void main(String[] args){
    	int[] days = {0,1,1,0,1,1,0};
    	DayChange d = new DayChange();
    	int[] output = d.Solution(days, 1);
    	for(int item : output)
    		System.out.println(item);
    }
}
