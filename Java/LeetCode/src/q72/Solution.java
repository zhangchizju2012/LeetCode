package q72;

public class Solution {
    public int minDistance(String word1, String word2) {
    	int length1 = word1.length();
    	int length2 = word2.length();
    	int[][] result = new int[length1+1][length2+1];
    	for(int i=0;i<length1+1;i++){
    		result[i][0] = i;
    	}
    	for(int i=0;i<length2+1;i++){
    		result[0][i] = i;
    	}
    	for(int i=1;i<length1+1;i++){
    		for(int j=1;j<length2+1;j++){
    			if (word1.substring(i-1,i).equals(word2.substring(j-1,j))) {
					result[i][j] = result[i-1][j-1];
				}else{
					result[i][j] = Math.min(Math.min(result[i-1][j-1],result[i][j-1]),result[i-1][j])+1;
				}
    		}
    	}
        return result[length1][length2];
    }
}

//public class Solution {
//	HashMap<Integer[], Integer> result = new HashMap<Integer[], Integer>();
//	String word1;
//	String word2;
//    public int minDistance(String word1, String word2) {
//    	int length1 = word1.length();
//    	int length2 = word2.length();
//    	this.word1 = word1;
//    	this.word2 = word2;
//    	for(int i=0;i<length1+1;i++){
//    		Integer[] temp = new Integer[] {i,0};
//    		result.put(temp, i);
//    	}
//    	for(int i=0;i<length2+1;i++){
//    		Integer[] temp = new Integer[] {0,i};
//    		result.put(temp, i);
//    	}
//        return helper(length1, length2);
//    }
//    public int helper(int i, int j){
//    	int temp;
//    	Integer[] key = new Integer[] {i,j};
//    	if(result.containsKey(key)==false){
//    		System.out.println(i);
//    		System.out.println(j);
//    		if(word1.charAt(i-1) == word2.charAt(j-1)){
//    			temp = helper(i-1, j-1);
//    		}
//    		else{
//    			temp = Math.min(Math.min(helper(i-1, j-1), helper(i-1, j)),helper(i, j-1))+1;
//    		}
//    		result.put(key, temp);
//    	}
//    	return result.get(key);
//    }
//    public static void main(String[] args) {
//    	//String w1 = "rabbbiit";
//    	//String w2 = "rabbit";
//    	Solution s = new Solution();
//    	int result;
//    	result = s.minDistance("ra","r");
//    	System.out.println(result);
//    }
//}

//public class Solution {
//	HashMap<List<Integer>, Integer> result = new HashMap<List<Integer>, Integer>();
//	String word1;
//	String word2;
//    public int minDistance(String word1, String word2) {
//    	int length1 = word1.length();
//    	int length2 = word2.length();
//    	this.word1 = word1;
//    	this.word2 = word2;
//    	for(int i=0;i<length1+1;i++){
//    		List<Integer> temp = Arrays.asList(i,0);
//    		result.put(temp, i);
//    	}
//    	for(int i=0;i<length2+1;i++){
//    		List<Integer> temp = Arrays.asList(0,i);
//    		result.put(temp, i);
//    	}
//        return helper(length1, length2);
//    }
//    public int helper(int i, int j){
//    	int temp;
//    	List<Integer> key =  Arrays.asList(i,j);
//    	if(result.containsKey(key)==false){
//    		if(word1.charAt(i-1) == word2.charAt(j-1)){
//    			temp = helper(i-1, j-1);
//    		}
//    		else{
//    			temp = Math.min(Math.min(helper(i-1, j-1), helper(i-1, j)),helper(i, j-1)) + 1;
//    		}
//    		result.put(key, temp);
//    	}
//    	return result.get(key);
//    }
//    public static void main(String[] args) {
//    	//String w1 = "rabbbiit";
//    	//String w2 = "rabbit";
//    	Solution s = new Solution();
//    	int result;
//    	result = s.minDistance("rabbbbiit","rabbit");
//    	System.out.println(result);
//    }
//}
