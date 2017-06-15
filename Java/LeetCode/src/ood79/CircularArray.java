package ood79;

import java.util.Iterator;

public class CircularArray <T> implements Iterable<T>{
//public class CircularArray <T,E> implements Iterator<E>{
//前面的是占位符，为后面的E赋值，为里面的T赋值，T,E需要在初始化变量的时候指定
//（Iterator后面跟的E是导致next()方法的return类型为E,这里的E由<T,E>里的E决定
	T[] array;
	int start = 0;
	int length;
	public CircularArray(int length) {
		// array = new T[length]; // cannot create a generic array of T
		// https://stackoverflow.com/questions/529085/how-to-create-a-generic-array-in-java
		array = (T[]) new Object[length];
		this.length = length;
	}
	public int convert(int index){
		if(index>=length){
			throw new java.lang.IndexOutOfBoundsException("Index "+index+" is out of bouds.");
		}
		if(start+index>=length){
			return start + index - length;
		}
		else{
			return start + index;
		}
	}
	public void rotate(int index){
		start = convert(index);
	}
	public T get(int index){
		return array[convert(index)];
	}
	public void set(int index, T item){
		array[convert(index)] = item;
	}
	@Override
	// inspired by https://codereview.stackexchange.com/questions/48109/simple-example-of-an-iterable-and-an-iterator-in-java
	public Iterator<T> iterator() {
		// TODO Auto-generated method stub
		return new CircularArrayIterator();
	}
	private class CircularArrayIterator implements Iterator<T>{
		int point;
		public CircularArrayIterator() {
			// TODO Auto-generated constructor stub
			point = 0; //每次调用这个迭代器需要将point置为0，如果不用这个内部类，就不存在这么一个可以调用就置为0的东西
		}
		@Override
		public boolean hasNext() {
			// TODO Auto-generated method stub
			return point < length;
		}
		@Override
		public T next() {
			// TODO Auto-generated method stub
			point += 1;
			return get(point-1);
		}
		
	}
	
}
