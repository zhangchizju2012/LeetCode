package test;

//import java.util.AbstractMap;
//import java.util.HashMap;
//import java.util.LinkedHashMap;
//import java.util.TreeMap;
//
//public class test {
//	public static void insertAndPrint(AbstractMap<String, String> map) {
//		String[] array = {"ab","aa","a"};
//		for (String x : array) {
//			map.put(x, x);
//		}
//		
//		for (String k : map.keySet()) {
//			System.out.print(k + ", ");
//		}
//	}
//	
//	public static void main(String[] args) {
//		TreeMap<String, String> treeMap = new TreeMap<String, String>();
//		HashMap<String, String> hashMap = new HashMap<String, String>();
//		LinkedHashMap<String, String> linkedHashMap = new LinkedHashMap<String, String>();
//		
//		System.out.println("\nHashMap - Arbitrary Order:");
//		insertAndPrint(hashMap);
//		
//		System.out.println("\nLinkedHashMap - Insertion Order:");
//		insertAndPrint(linkedHashMap);
//
//		System.out.println("\nTreeMap - Natural Order:");
//		insertAndPrint(treeMap);
//	}
//
//}

import java.util.ArrayList;

public class test {
	int kk;
	public static void main(String[] args) {
		String s = "12";
		System.out.println(s);
		s = s + "3";
		System.out.println(s);
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
