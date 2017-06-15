package ood79;

public class TestArray {
	public static void main(String[] args){
		CircularArray<Integer> array = new CircularArray<>(5);
		for(int i=0;i<5;i++){
			array.set(i, i);
		}
		array.rotate(2);
		array.set(1, 9);
		//System.out.println(array.get(1));
		for(int i=0;i<5;i++){
			System.out.println(array.get(i));
		}
		for(int item:array){
			System.out.println(item);
		}
		for(int item:array){
			System.out.println(item);
		}
	}
}
