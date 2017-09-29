/**
 * @author zhangchi
 *
 * 2017年9月28日 下午1:55:04
 */
package amazon;

/**
 * @author zhangchi
 * 2017年9月28日 下午1:55:04
 */
public class GreatestCommonDivisor {
	public int solution(int[] array) {
        if(array == null || array.length == 0){return 0;}
	    int length = array.length;
        int result = array[0];
        for(int i = 1; i < length; i++){
            result = gcd(array[i], result);
        }
        return result;
	}
	// 辗转相除法
    public int gcd(int value1, int value2){
        if(value1 < value2){
            int temp = value1;
            value1 = value2;
            value2 = temp;
        }
        int next = value1 % value2;
        while(next != 0){
            value1 = value2;
            value2 = next;
            next = value1 % value2;
        }
        return value2;
    }
    public static void main(String[] args){
    	int[] input = {6,12};
    	GreatestCommonDivisor greatestCommonDivisor = new GreatestCommonDivisor();
    	System.out.println(greatestCommonDivisor.solution(input));
    }
}
