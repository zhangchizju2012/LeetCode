/**
 * @author zhangchi
 *
 * 2017年9月28日 下午10:51:46
 */
package amazon;

import java.util.Arrays;

/**
 * @author zhangchi
 * 2017年9月28日 下午10:51:46
 */
public class FourInteger {
	public int[] Solution(int a, int b, int c, int d){
		int[] result = {a,b,c,d};
		Arrays.sort(result);
		for(int item:result)
			System.out.println(item);
		swap(result, 0, 1);
		swap(result, 2, 3);
		swap(result, 0, 3);
		return result;
	}
	public void swap(int[] input, int i, int j){
		int temp = input[i];
		input[i] = input[j];
		input[j] = temp;
		//return input;
	}
	public static void main(String[] args){
		FourInteger f = new FourInteger();
		int[] result = f.Solution(1, 2, 3, 4);
		for(int item: result)
			System.out.println(item);
	}
}
