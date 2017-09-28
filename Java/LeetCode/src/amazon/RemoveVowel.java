/**
 * @author zhangchi
 *
 * 2017年9月27日 下午8:49:27
 */
package amazon;

/**
 * @author zhangchi
 * 2017年9月27日 下午8:49:27
 */
public class RemoveVowel {
	public String removeVowel(String string){
        StringBuffer sb = new StringBuffer();
        String check = "aeiouAEIOU";
        int length = string.length();
        for(int i=0;i<length;i++){
            //String temp = string.substring(i,i+1);
            char temp = string.charAt(i);
            //System.out.println(temp);
            if(check.indexOf(temp) == -1){
                sb.append(temp);
            }
        }
        return sb.toString();
    }
	public static void main(String[] args){
		RemoveVowel removeVowel = new RemoveVowel();
		System.out.println(removeVowel.removeVowel("abec"));
	}
}
