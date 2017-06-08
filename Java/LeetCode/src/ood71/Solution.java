package ood71;

public class Solution {
	public static void main(String[] args){
		// 学会如何根据public class Hand <T extends Card> 来new出新的对象
//		Hand<Card> temp = new Hand<>();
//		// 学会如何使用enum
//		Suit suit = Suit.Club;
//		Card card = new Card(3,suit) {
//			
//			@Override
//			public int value() {
//				// TODO Auto-generated method stub
//				return 0;
//			}
//		};
//		temp.addCard(card);
//		temp.print();
		BlackJackHand temp = new BlackJackHand();
		//BlackJackHand<Card> temp = new BlackJackHand<>();
		// 学会如何使用enum
		Suit suit = Suit.Club;
		BlackJackCard card = new BlackJackCard(3,suit);
		temp.addCard(card);
		temp.print();
	}
}
