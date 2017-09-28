/**
 * @author zhangchi
 *
 * 2017年9月27日 下午8:38:33
 */
package amazon;

import java.util.List;
import java.util.ArrayList;

/**
 * @author zhangchi
 * 2017年9月27日 下午8:38:33
 */
// 基本思路是根据之前的东西，在bit模式处的头加1，然后倒序循环过去
public class GrayCode {
	public List<Integer> grayCode(int n) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        result.add(0);
        int index = 0;
        while(index<n){
            int value = (int)Math.pow(2,index);
            int length = result.size();
            for(int i=length-1;i>=0;i--){
                result.add(result.get(i)+value);
            }
            index += 1;
        }
        return result;
    }
}
