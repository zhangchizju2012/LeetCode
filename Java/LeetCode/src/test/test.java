package test;

import java.util.ArrayList;

public class test {
	int kk;
	public static void main(String[] args) {
		ArrayList<Integer> test2 = new ArrayList<>(10);
		System.out.println(test2.size());
		test hh = new test();
		ArrayList<Integer> test = new ArrayList<>();
		test.add(1);
		int c = 16;
		byte b = (byte)c;
		System.out.println(b);
		//test.remove(test.size()-1);
		System.out.println(hh.kk);
		String a = "123";
		System.out.println(a);
		System.out.println("123".substring(1, 2));
		System.out.println("123".contains("1"));
		test.remove(test.lastIndexOf(1));
		System.out.println(test);
	    System.out.println("Hello World!");
	}
}
