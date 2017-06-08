package ood71myself;

import java.util.ArrayList;

public abstract class Hand <T extends Card> {
	ArrayList<T> cards;
//	public Hand(ArrayList<T> cs) {
//		// TODO Auto-generated constructor stub
//		cards = cs;
//	}
	public void addCard(T card){
		cards.add(card);
	}
	public abstract int getPoint();
}
