/**
 * @author zhangchi
 *
 * 2017年7月28日 下午1:27:35
 */
package q115;

//Given a string S and a string T, count the number of distinct subsequences of S which equals T.
//
//A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
//
//Here is an example:
//S = "rabbbit", T = "rabbit"
//
//Return 3.

/**
 * @author zhangchi
 * 2017年7月28日 下午1:27:35
 */
public class Solution {
	public static void main(String[] args){
		Solution solution = new Solution();
		String s = "rabbbit";
		String t = "rabbit";
		System.out.println(solution.numDistinct(s, t));
	}
	public int numDistinct(String s, String t) {
		int lengthS = s.length();
		int lengthT = t.length();
		int[][] result = new int[lengthS+1][lengthT+1];
		for(int i=1;i<lengthT+1;i++){
			result[0][i] = 0;
		}
		for(int i=0;i<lengthS+1;i++){
			result[i][0] = 1;
		}
		for(int j=1;j<lengthT+1;j++){
			for(int i=1;i<lengthS+1;i++){
				if(s.charAt(i-1)==t.charAt(j-1)){
					// result[i-1][j-1]表示最后一个单词进行匹配，前面的按前面的数量算
					// result[i-1][j]表示放弃s的最后一个字母
					result[i][j] = result[i-1][j-1] + result[i-1][j];
				}else{
					result[i][j] = result[i-1][j];
				}
			}
		}
		return result[lengthS][lengthT];
	}
}
