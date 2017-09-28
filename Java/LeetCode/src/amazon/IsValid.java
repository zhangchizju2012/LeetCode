/**
 * @author zhangchi
 *
 * 2017年9月27日 下午9:17:04
 */
package amazon;

/**
 * @author zhangchi
 * 2017年9月27日 下午9:17:04
 */
public class IsValid {
	public int isValid(String string){
        //Stack<Character> stack = new Stack<Character>();
        int stack = 0;
        int length = string.length();
        String temp;
        for(int i=0;i<length;i++){
            temp = string.substring(i,i+1);
            if(temp.equals("(")){
                stack += 1;
            }else{
                if(stack>0){
                    stack -= 1;
                }else{
                    return -1;
                }
            }
        }
        if(stack!=0){
        	return -1;
        }else{
        return length / 2;}
    }
	public static void main(String[] args){
		IsValid isValid = new IsValid();
		String string = "(())()";
		System.out.println(isValid.isValid(string));
	}
}
