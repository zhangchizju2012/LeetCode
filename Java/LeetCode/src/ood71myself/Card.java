package ood71myself;

public abstract class Card {
	int value;
	int color;
	public Card(int v, int c){
		value = v;
		color = c;
	}
	public abstract int getPoint();
	public int getValue(){
		return value;
	}
	public int getColor(){
		return color;
	}
}
