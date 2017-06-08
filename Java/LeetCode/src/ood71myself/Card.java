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
	public void print(){
		System.out.print(value);
		switch (color) {
		case 1:
			System.out.print(" 红桃; ");
			break;
		case 2:
			System.out.print(" 方块; ");
			break;
		case 3:
			System.out.print(" 草花; ");
			break;
		case 4:
			System.out.print(" 黑桃; ");
			break;
		}
	}
}
