package q240;

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
    	Integer row = matrix.length;
    	if (row == 0){
    		return false;
    	}
    	Integer rowLen = matrix[0].length;
    	if (rowLen == 0){
    		return false;
    	}
    	Integer x = 0;
    	Integer y = rowLen - 1;
    	while (x < row && y >= 0){
            int temp = matrix[x][y];
            if (temp == target){
                return true;
            }
            else if (temp > target){
                y -= 1;
            }
            else{
                x += 1;
            }
    	}
        return false;
    }
}