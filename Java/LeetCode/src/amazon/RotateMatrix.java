/**
 * @author zhangchi
 *
 * 2017年9月21日 下午4:28:20
 */
package amazon;

/**
 * @author zhangchi
 * 2017年9月21日 下午4:28:20
 */
public class RotateMatrix {
	public int[][] rotate(int[][] matrix, int flag){
		int row, length;
		int n = matrix.length;
		int value;
		if(n%2==1){
			row = n / 2;
			length = n / 2 + 1;
		}else{
			row = length = n / 2;
		}
		for(int i=0;i<row;i++){
			for(int j=0;j<length;j++){
				value = matrix[i][j];
				matrix[i][j] = matrix[n-1-j][i];
				matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
				matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
				matrix[j][n-1-i] = value;
			}
		}
		return matrix;
	}
	public static void main(String[] args){
		RotateMatrix s = new RotateMatrix();
		int[][] input = new int[4][4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				input[i][j] = 4 * i + j;
				System.out.print(input[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println("------------");
		int[][] output = s.rotate(input, 0);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				System.out.print(output[i][j]+" ");
			}
			System.out.println();
		}
//		int[][] input = new int[5][5];
//		for(int i=0;i<5;i++){
//			for(int j=0;j<5;j++){
//				input[i][j] = 5 * i + j;
//				System.out.print(input[i][j]+" ");
//			}
//			System.out.println();
//		}
//		System.out.println("------------");
//		int[][] output = s.rotate(input, 0);
//		for(int i=0;i<5;i++){
//			for(int j=0;j<5;j++){
//				System.out.print(output[i][j]+" ");
//			}
//			System.out.println();
//		}
	}
}
