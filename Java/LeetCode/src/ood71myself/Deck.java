package ood71myself;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public abstract class Deck <T extends Card, E extends Hand<T>>{
	ArrayList<T> cards = new ArrayList<>();
	int index;
	public abstract void initialize();
	public void shuffle(){
		long seed = System.nanoTime();
		Collections.shuffle(cards, new Random(seed));
	}
	public T getNextCard(){
		if(index < cards.size()){
			T temp = cards.get(index);
			index += 1;
			return temp;
		}else{
			return null;
		}
	}
	public abstract E[] givePlayerInitialCard(int playerNumber);
	//public abstract Hand<T>[] givePlayerInitialCard(int playerNumber);
	public boolean left(){
		if(index < cards.size()){
			return true;
		}else{
			return false;
		}
	}
}

//public abstract class Deck <T extends Card>{
//	ArrayList<T> cards = new ArrayList<>();
//	int index;
//	public abstract void initialize();
//	public void shuffle(){
//		long seed = System.nanoTime();
//		Collections.shuffle(cards, new Random(seed));
//	}
//	public T getNextCard(){
//		if(index < cards.size()){
//			T temp = cards.get(index);
//			index += 1;
//			return temp;
//		}else{
//			return null;
//		}
//	}
//	public abstract Hand<T>[] givePlayerInitialCard(int playerNumber);
//	public boolean left(){
//		if(index < cards.size()){
//			return true;
//		}else{
//			return false;
//		}
//	}
//}