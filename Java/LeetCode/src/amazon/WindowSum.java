/**
 * @author zhangchi
 *
 * 2017年9月21日 下午3:53:06
 */
package amazon;

import java.util.ArrayList;
import java.util.List;

/**
 * @author zhangchi
 * 2017年9月21日 下午3:53:06
 */
public class WindowSum {
	public ArrayList<Integer> getWindowSum(List<Integer> list, int k){
		if(k>list.size()){
			return null;
		}
		ArrayList<Integer> result = new ArrayList<>();
		int value = 0;
		for(int i=0;i<k;i++){
			value += list.get(i);
		}
		result.add(value);
		for(int i=k;i<list.size();i++){
			value = value - list.get(i-k) + list.get(i);
			result.add(value);
		}
		return result;
	}
	
	public static void main(String[] args){
		WindowSum s =  new WindowSum();
		ArrayList<Integer> input = new ArrayList<>();
		input.add(1);
		input.add(2);
		input.add(3);
		input.add(4);
		input.add(5);
		System.out.println(input);
		System.out.println(s.getWindowSum(input, 4));
	}
}
