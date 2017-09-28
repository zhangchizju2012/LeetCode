/**
 * @author zhangchi
 *
 * 2017年9月27日 下午10:57:07
 */
package amazon;

/**
 * @author zhangchi
 * 2017年9月27日 下午10:57:07
 */
public class LongestPalindromicSubstring {
	public String longestPalindrome(String s) {
        int length = s.length();
        int temp = 0;
        String result = null;
        for(int index=0;index<length;index++){
            if(index-temp-1>=0 && check(s.substring(index-temp-1,index+1))){
                result = s.substring(index-temp-1,index+1);
                temp += 2;
            }else if(check(s.substring(index-temp,index+1))){
                result = s.substring(index-temp,index+1);
                temp += 1;
            }
        }
        return result;
    }
    public boolean check(String s){
        StringBuffer sb = new StringBuffer(s);
        return s.equals(sb.reverse().toString());
    }
}
