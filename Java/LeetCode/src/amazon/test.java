/**
 * @author zhangchi
 *
 * 2017年9月22日 上午11:16:38
 */
package amazon;

import java.util.ArrayList;

/**
 * @author zhangchi
 * 2017年9月22日 上午11:16:38
 */
class Base {
	 protected int value;
//	 public Base(){
//		 
//	 }
//	 public Base( int initValue ) {
//	 // implicitly inserted call to super()
//	System.out.println("1");
//	 value = initValue;
//	 }
	}
class Derived extends Base {
 public Derived( int initValue ) {
	 //super(initValue);
	 System.out.println("2");
	 //value = initValue;
 // explicit call to super( … );
 // super( … ) if used, must come first
 }
}
public class test{
	public static void main(String[] args){
		Derived derived = new Derived(1);
		StringBuffer sb = new StringBuffer("abc");
		String a = null;
		char b = 'b';
		System.out.println(sb.equals(sb.reverse()));
		System.out.println(sb.substring(0, 2));
		
		
	}
}

//public class test {
//	public static void main(String[] args){
//		ArrayList<Integer> a = new ArrayList<>();
//		ArrayList<Integer> b = new ArrayList<>();
//		System.out.println(a.equals(b));
//		System.out.println(a==b);
//		ArrayList<Integer> c = a;
//		System.out.println(a.equals(c));
//		System.out.println(a==c);
//	}
//}
