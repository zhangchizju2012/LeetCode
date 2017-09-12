/**
 * @author zhangchi
 *
 * 2017年9月10日 下午3:06:17
 */
package q130;
import java.util.HashMap;

/**
 * @author zhangchi
 * 2017年9月10日 下午3:06:17
 */
class Solution {
    public void solve() {
        //int row = board.length;
        //int length = board[0].length;
        HashMap<Integer[][], Character> dic = new HashMap<>();
        Integer[][] a = new Integer[2][2];
        for(int i=0;i<2;i++){
        	for(int j=0;j<2;j++){
        		a[i][j] = i + j;
        	}
        }
        Character[] b = {'a','b'};
        char c = 'c';
        dic.put(a, b[0]);
        for(Integer[][] item:dic.keySet()){
        	System.out.println(dic.get(item));
        }
        System.out.println("123");
    }
    public static void main(String[] args){
    	Solution s = new Solution();
    	s.solve();
    }
}