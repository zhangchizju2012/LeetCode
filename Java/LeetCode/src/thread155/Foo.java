package thread155;

import java.util.concurrent.Semaphore;

// acquire相当于拿到了一张通行证，new Semaphore(1)说明只有一张通行证
// 所以如果first()如果没有执行，那么sm1唯一的一张通行证则还没被释放
// 所以second第一行在索取通信证就无法被执行（但并不算exception）,所以second之后的内容也就无法被执行
// 直到运行完first()并将通行证释放出来，second()才能执行
public class Foo implements Runnable{
	Semaphore sm1, sm2;
	public Foo(){
		sm1 = new Semaphore(1);
		sm2 = new Semaphore(1);
		try {
			sm1.acquire();
			sm2.acquire();
		} catch (Exception e) {
			// TODO: handle exception
		}
	}
	public void first() {
		System.out.println("First."); 
		sm1.release();
	} 
	public void second() { 
		try {
			sm1.acquire();
			sm1.release();
			System.out.println("Second.");
			sm2.release();
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("fuck");
		}
	} 
	public void third() {
		try {
			sm2.acquire();
			sm2.release();
			System.out.println("Third.");
		} catch (Exception e) {
			// TODO: handle exception
		}
	} 
	@Override
	public void run() {
		// TODO Auto-generated method stub
		if(Thread.currentThread().getName().equals("first")){
			first();
		}else if (Thread.currentThread().getName().equals("second")) {
			second();
		}else if (Thread.currentThread().getName().equals("third")) {
			third();
		}
	}
	public static void main(String[] args){
		Foo job = new Foo();
		Thread one = new Thread(job);
		Thread two = new Thread(job);
		Thread three = new Thread(job);
		one.setName("first");
		two.setName("second");
		three.setName("third");
		three.start();
		two.start();
		one.start();
	}

}
//开始版本：三个顺序不一定

//package thread155;
//
//public class Foo implements Runnable{
//	public void first() { 
//		System.out.println("First."); 
//	} 
//	public void second() { 
//		System.out.println("Second.");
//	} 
//	public void third() {
//		System.out.println("Third.");
//	} 
//	@Override
//	public void run() {
//		// TODO Auto-generated method stub
//		if(Thread.currentThread().getName().equals("first")){
//			first();
//		}else if (Thread.currentThread().getName().equals("second")) {
//			second();
//		}else if (Thread.currentThread().getName().equals("third")) {
//			third();
//		}
//	}
//	public static void main(String[] args){
//		Foo job = new Foo();
//		Thread one = new Thread(job);
//		Thread two = new Thread(job);
//		Thread three = new Thread(job);
//		one.setName("first");
//		two.setName("second");
//		three.setName("third");
//		one.start();
//		two.start();
//		three.start();
//	}
//
//}
