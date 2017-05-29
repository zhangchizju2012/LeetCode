package test;

class board {
	public int bark(){
		System.out.println("456");
		return 1;
	}
}

class Snowboard extends board{
	public int hashCode(){
	//public int bark(){
		System.out.println("123");
		return 1;
	}
	public int bark(){
		System.out.println("shit");
		return 1;
	}
}

public class objectTest {
	public static void main(String[] args){
		//Object o = new Snowboard();
		Snowboard s = new Snowboard();
		//Object o = s;
		board o = s;
		o.hashCode();
		o.bark();
		//Snowboard temp = (Snowboard) o;
		//temp.bark();
	}
}
