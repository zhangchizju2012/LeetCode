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
		Object o = new Snowboard();
		//Snowboard s = new Snowboard();
		//Object o = s;
		//board o = s;
		o.hashCode();
		//o.bark();
		//Snowboard temp = (Snowboard) o;
		//temp.bark();
	}
}
//子类overriding了父类的方法，调用的时候会调用子类的方法，但是子类多出来的function，不能按以下的方式调用（见1）
////(1)
//Object o = new Snowboard();
//o.hashCode(); //123
//o.bark(); //不行 -->因为object没有bard()
////(2)
//Snowboard s = new Snowboard();
//board o = s;
//o.hashCode(); //123
//o.bark(); //shit

