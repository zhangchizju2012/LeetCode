package thread153;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Chopstick {
	private Lock lock;
	
	public Chopstick() {
		lock = new ReentrantLock();
	}

	public boolean pickUp() {
		return lock.tryLock();//这个类的某个实例被lock了之后，该实例就不能被别的进程动到
	}
	
	public void putDown() {
		lock.unlock();	
	}
}
