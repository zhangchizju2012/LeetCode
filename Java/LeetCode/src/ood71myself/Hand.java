package ood71myself;

import java.util.ArrayList;

public abstract class Hand <T extends Card> {
	// <>就相当于一个占位符，个人理解，然后之后程序里要用到<>里的这种类型(也就相当于是一个参数)
	// 在new新对象和extends这个类的时候都要带上这个<>，
	// 定义函数返回值用到这个类的时候也要用到<>，看Deck.class line24,只不过那里还是个数组，所以多了[]
	ArrayList<T> cards = new ArrayList<>();
	int name;
	public Hand(ArrayList<T> cs) {
		// TODO Auto-generated constructor stub
		cards = cs;
	}
	// 构造函数这里还有些疑问
	public Hand(){
		
	}
	public void addCard(T card){
		cards.add(card);
	}
	public abstract int getPoint();
	public void setPlayerName(int name){
		this.name = name;
	}
	public int getPlayerName(){
		return name;
	}
	public ArrayList<T> getCards(){
		return cards;
	}
}
