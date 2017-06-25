package ood712;

public class TestHash {
	public static void main(String[] args){
		Hash<String, Integer> hashTest = new Hash<>();
		hashTest.put("123", 2);
		System.out.println(hashTest.get("123"));
	}
}
