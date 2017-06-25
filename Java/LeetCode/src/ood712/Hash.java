package ood712;

import java.util.ArrayList;

public class Hash <K,V> {
	public class LinkedListNode {
//		LinkedListNode prev = null;
		LinkedListNode next = null;
		K key = null;
		V value = null;
		public LinkedListNode() {}
		public LinkedListNode(K k, V v) {
			key = k;
			value = v;
		}
//		public void setPrev (LinkedListNode p){
//			prev = p;
//		}
		public void setNext (LinkedListNode n){
			next = n;
		}
	}
	// 这里加了(10)似乎没什么用，就算加了10，dict.size()还是会返回0
	ArrayList<LinkedListNode> dict = new ArrayList<>();//(10);
	
	public Hash() {
//		for(LinkedListNode item:dict){
//			item = new LinkedListNode();
//		}
		for(int i=0;i<10;i++){
//			dict.add(i, new LinkedListNode());
			dict.add(null);
			// 注意add和set的区别
		}
	}
	public int hashFunction(K k){
		System.out.println(dict.size());
		return k.toString().length() % dict.size();
	}
	// 还有问题，放入的key可能之前放过，这次是更新value值
	public void put(K k, V v){
		int index = hashFunction(k);
		if(dict.get(index) == null){
			//dict.get(index) = new LinkedListNode(k,v); //这个是不行的
			dict.set(index, new LinkedListNode(k,v));
		}else{
//		LinkedListNode previous = null;
		LinkedListNode now = dict.get(index);
		while(now!=null){
//			previous = now;
			now = now.next;
		}
		now = new LinkedListNode(k,v);
//		now.setPrev(previous);
		}
	}
	public boolean checkIn(K k){
		int index = hashFunction(k);
		LinkedListNode now = dict.get(index);
		while(now!=null){
			if(now.key==k){
				return true;
			}else{
				now = now.next;
			}
		}
		//throw exception 
		return false;
	}
	public V get(K k){
		int index = hashFunction(k);
		LinkedListNode now = dict.get(index);
		while(now!=null){
			if(now.key==k){
				return now.value;
			}else{
				now = now.next;
			}
		}
		//throw exception 
		System.out.println("not in the hash");
		return null;
	}
	public V pop(K k){
		int index = hashFunction(k);
		LinkedListNode previous = null;
		LinkedListNode now = dict.get(index);
		while(now!=null){
			if(now.key==k){
				previous.next = now.next;
				return now.value;
			}else{
				previous = now;
				now = now.next;
			}
		}
		//throw exception 
		//ystem.out.println("not in the hash");
		return null;
	}
}
