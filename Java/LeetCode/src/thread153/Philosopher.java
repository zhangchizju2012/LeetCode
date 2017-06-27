package thread153;

import CtCILibrary.AssortedMethods;

//lock是哪个进程上的lock 哪个进程负责unlock --> P457,在没有被unlock前，全都归属这个进程
public class Philosopher extends Thread {
	private final int maxPause = 100;
	private int bites = 3;
	
	private Chopstick left;
	private Chopstick right;
	private int index;
	public Philosopher(int i, Chopstick left, Chopstick right) {
		index = i;
		this.left = left;
		this.right = right;
		//this.left.pickUp();//自己加的，（相当于->用于修饰同时）保证了同时拿起左快子，这样就肯定是deadlocks，
		//去掉这一行就可能deadlock可能没有,因为去掉就没有保证同时拿起左快子
		//但是这样也不好，因为lock是哪个进程上的lock 哪个进程负责unlock --> P457
	}
	
	public void eat() {
		System.out.println("Philosopher " + index + ": start eating");
		if (pickUp()) {// 这里通过if else，以及chopstick的pickUp()采用的是tryLock()而不是lock(),只是模仿了
			// deadlock的现象，程序还是会继续跑，没有真的deadlock，如果用lock()，就会真的卡在这里，
			// 直到被unlock()，才能运行下去
			chew();
			putDown();
			System.out.println("Philosopher " + index + ": done eating");
		} else {
			//left.putDown();//这样不行，因为lock是哪个进程上的lock 哪个进程负责unlock
			System.out.println("Philosopher " + index + ": gave up on eating");
		}
	}
	
	public boolean pickUp() {
		pause();
		if (!left.pickUp()) {
			return false;
		} 
		pause();
		if (!right.pickUp()) {
			//left.putDown();
			return false;
		} 
		pause();
		return true;
	}
	
	public void chew() {
		System.out.println("Philosopher " + index + ": eating");
		pause();
	}
	
	public void pause() {
		try {
			int pause = AssortedMethods.randomIntInRange(0, maxPause);
			Thread.sleep(pause);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public void putDown() {
		right.putDown();
		left.putDown();
	}
	
	public void run() {
		for (int i = 0; i < bites; i++) {
			eat();
		}
	}
}
